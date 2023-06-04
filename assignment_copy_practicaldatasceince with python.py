import os
import sys

class Customer:
    BOOKING_FEE_PER_TICKET = 2
    def __init__(self, customer_id, name):
        self._id = customer_id
        self._name = name
        self._discount_rate = 0

    @property
    def get_id(self):
        return self._id

    @property
    def get_name(self):
        return self._name

    def get_discount(self, cost):
        return self._discount_rate * cost
    
    def set_discount_rate(self, new_discount_rate):
        if new_discount_rate <= 0:
            raise ValueError("Invalid discount rate. Please enter a positive value.")
        self._discount_rate = new_discount_rate
    
    @classmethod
    def get_booking_fee(cls,ticket_quantity):
        return cls.BOOKING_FEE_PER_TICKET * ticket_quantity

    def display_info(self):
        print(f"ID: {self._id}, name: {self._name}")
        
    def class_name(self):
        print(f"{self._name} is Standard Customer")


class RewardFlatCustomer(Customer):
    def __init__(self,customer_id, name, discount_rate=0.2):
        super().__init__(customer_id, name)
        self._discount_rate = discount_rate

    @property
    def discount_rate(self):
        return self._discount_rate

    def get_discount(self, cost):
        return cost * self._discount_rate

    def display_info(self):
        print(f"ID: {self._id}, name: {self._name}, discount rate: {self._discount_rate}")

    def set_discount_rate(self, new_discount_rate):
        if new_discount_rate <= 0:
            raise ValueError("Invalid discount rate. Please enter a positive value.")
        self._discount_rate = new_discount_rate
               
    def class_name(self):
        print(f"{self._name} is Reward Flat Customer")

class RewardStepCustomer(Customer):
    def __init__(self, customer_id, name, discount_rate=0.3, threshold=50):
        super().__init__(customer_id, name)
        self._discount_rate = discount_rate
        self._threshold = threshold

    @property
    def discount_rate(self):
        return self._discount_rate

    @property
    def threshold(self):
        return self._threshold

    def get_discount(self, cost):
        if cost >= self._threshold:
            return cost * self._discount_rate
        else:
            return 0

    def display_info(self):
        print(f"ID: {self._id}, name: {self._name}, discount rate: {self._discount_rate}, threshold: {self._threshold}")

    def set_discount_rate(self, new_discount_rate):
        if new_discount_rate <= 0:
            raise ValueError("Invalid discount rate. Please enter a positive value.")
        self._discount_rate = new_discount_rate

    def set_threshold(self, new_threshold):
        if new_threshold <= 0:
            raise ValueError("Invalid threshold. Please enter a positive value.")
        self._threshold = new_threshold     
    
    def class_name(self):
        print(f"{self._name} is Reward Step Customer")


class Movie:
    def __init__(self, movie_id, name, seat_available):
        self._movie_id = movie_id
        self._name = name
        self._seat_available = seat_available
        
    @property    
    def get_id(self):
        return self._movie_id
    
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_seats(self):
        return self._seat_available
        
    def update_seats(self, new_seats):
        self._seat_available = new_seats
    
    def display_info(self):
        print(f"ID: {self._movie_id}, name: {self._name}, seats available: {self._seat_available}")


class Ticket:
    def __init__(self, ticket_id, ticket_type, price):
        self._ticket_id = ticket_id
        self._ticket_type = ticket_type
        self._price = price
    
    @property    
    def get_id(self):
        return self._ticket_id
    
    @property
    def get_type(self):
        return self._ticket_type
    
    @property
    def get_price(self):
        return self._price
    
    def display_info(self):
        print(f"ID: {self._ticket_id}, type: {self._ticket_type}, price: {self._price}")


class GroupTicket(Ticket):
    def __init__(self, ticket_id, ticket_type, price, num_tickets):
        super().__init__(ticket_id, ticket_type, price)
        self._num_tickets = num_tickets
    
    def get_price(self):
        return self._price * self._num_tickets
    
    def display_info(self):
        print(f"ID: {self._ticket_id}, type: {self._ticket_type}, price per ticket: {self._price}, number of tickets: {self._num_tickets}, total price: {self.get_price()}")


class Booking:
    def __init__(self, customer, movie, ticket, quantity):
        self._customer = customer
        self._movie = movie
        self._ticket = ticket
        self._quantity = quantity

    def compute_cost(self):
        ticket_price = self._ticket.get_price
        total_price = ticket_price * self._quantity
        discount = self._customer.get_discount(total_price)
        booking_fee = Customer.get_booking_fee(self._quantity)
        cost = total_price - discount + booking_fee
        return cost
    
    def display_info(self):
        print("Booking details:")
        self._customer.display_info()
        self._movie.display_info()
        self._ticket.display_info()
        print(f"Quantity: {self._quantity}")
        print(f"Total cost: {self.compute_cost()}")
        

class Records:
    def __init__(self):
        self._customers = {}
        self._movies = {}
        self._tickets = {}

    def add_customer(self, customer):
        self._customers[customer.get_id] = customer

    def add_movie(self, movie):
        self._movies[movie.get_id] = movie

    def add_ticket(self, ticket):
        self._tickets[ticket.get_id] = ticket

    def read_customer_data(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    customer_id = int(data[0])
                    name = data[1]
                    discount_rate = float(data[2])
                    customer_type = data[3]

                    if customer_type == "Standard":
                        customer = Customer(customer_id, name)
                    elif customer_type == "RewardFlat":
                        customer = RewardFlatCustomer(customer_id, name, discount_rate)
                    elif customer_type == "RewardStep":
                        threshold = float(data[4])
                        customer = RewardStepCustomer(customer_id, name, discount_rate, threshold)
                    else:
                        print(f"Invalid customer type: {customer_type}. Skipping customer data.")
                        continue

                    self.add_customer(customer)
        except FileNotFoundError:
            print(f"File not found: {filename}. No customer data loaded.")

    def read_movie_data(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    movie_id = int(data[0])
                    name = data[1]
                    seats_available = int(data[2])
                    movie = Movie(movie_id, name, seats_available)
                    self.add_movie(movie)
        except FileNotFoundError:
            print(f"File not found: {filename}. No movie data loaded.")

    def read_ticket_data(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    ticket_id = int(data[0])
                    ticket_type = data[1]
                    price = float(data[2])

                    if ticket_type == "Group":
                        num_tickets = int(data[3])
                        ticket = GroupTicket(ticket_id, ticket_type, price, num_tickets)
                    else:
                        ticket = Ticket(ticket_id, ticket_type, price)

                    self.add_ticket(ticket)
        except FileNotFoundError:
            print(f"File not found: {filename}. No ticket data loaded.")

    def display_customer_info(self):
        for customer_id, customer in self._customers.items():
            customer.display_info()

    def display_movie_info(self):
        for movie_id, movie in self._movies.items():
            movie.display_info()

    def display_ticket_info(self):
        for ticket_id, ticket in self._tickets.items():
            ticket.display_info()


def main():
    records = Records()
    records.read_customer_data("customers.txt")
    records.read_movie_data("movies.txt")
    records.read_ticket_data("tickets.txt")
    records.display_customer_info()
    records.display_movie_info()
    records.display_ticket_info()

    # Example usage:
    customer_id = 1
    movie_id = 1
    ticket_id = 1
    quantity = 2

    customer = records._customers.get(customer_id)
    movie = records._movies.get(movie_id)
    ticket = records._tickets.get(ticket_id)

    if customer and movie and ticket:
        booking = Booking(customer, movie, ticket, quantity)
        booking.display_info()
    else:
        print("Invalid customer, movie, or ticket ID. Please check the input.")

if __name__ == "__main__":
    main()