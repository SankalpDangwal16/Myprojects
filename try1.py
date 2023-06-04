import os
import sys

class Customer:
    BOOKING_FEE_PER_TICKET = 2
    
    def __init__(self, customer_id, name):
        self._id = customer_id
        self._name = name
        self._discount_rate = 0

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def get_discount(self, cost):
        return self._discount_rate * cost
    
    def set_discount_rate(self, new_discount_rate):
        if new_discount_rate <= 0:
            raise ValueError("Invalid discount rate. Please enter a positive value.")
        self._discount_rate = new_discount_rate
    
    @classmethod
    def get_booking_fee(cls, ticket_quantity):
        return cls.BOOKING_FEE_PER_TICKET * ticket_quantity

    def display_info(self):
        print(f"ID: {self._id}, name: {self._name}")
        
    def class_name(self):
        print(f"{self._name} is a Standard Customer")


class RewardFlatCustomer(Customer):
    def __init__(self, customer_id, name, discount_rate=0.2):
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
        print(f"{self._name} is a Reward Flat Customer")

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
        print(f"{self._name} is a Reward Step Customer")


class Movie:
    def __init__(self, movie_id, name, seat_available):
        self._movie_id = movie_id
        self._name = name
        self._seat_available = seat_available
        
    @property    
    def id(self):
        return self._movie_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def seats_available(self):
        return self._seat_available

    def update_seats_available(self, seats_booked):
        if seats_booked <= self._seat_available:
            self._seat_available -= seats_booked
            return True
        else:
            return False

    def display_info(self):
        print(f"ID: {self._movie_id}, name: {self._name}, seats available: {self._seat_available}")


class Ticket:
    def __init__(self, ticket_id, ticket_type, price):
        self._ticket_id = ticket_id
        self._ticket_type = ticket_type
        self._price = price

    @property
    def id(self):
        return self._ticket_id

    @property
    def type(self):
        return self._ticket_type

    @property
    def price(self):
        return self._price

    def display_info(self):
        print(f"ID: {self._ticket_id}, type: {self._ticket_type}, price: {self._price}")


class GroupTicket(Ticket):
    def __init__(self, ticket_id, ticket_type, price, quantity):
        super().__init__(ticket_id, ticket_type, price)
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    def get_ticket_components(self):
        return f"ID: {self._ticket_id}, type: {self._ticket_type}, price: {self._price}, quantity: {self._quantity}"

    def display_info(self):
        print(self.get_ticket_components())


class Booking:
    def __init__(self, customer, movie, ticket):
        self._customer = customer
        self._movie = movie
        self._ticket = ticket

    @property
    def customer(self):
        return self._customer

    @property
    def movie(self):
        return self._movie

    @property
    def ticket(self):
        return self._ticket

    def get_total_cost(self):
        cost = self._ticket.price
        discount = self._customer.get_discount(cost)
        total_cost = cost - discount
        booking_fee = Customer.get_booking_fee(1)
        return total_cost + booking_fee

    def display_info(self):
        print("Booking Information:")
        self._customer.display_info()
        self._movie.display_info()
        self._ticket.display_info()
        print(f"Total cost: {self.get_total_cost()}")

class Records:
    def __init__(self):
        self._customers = []
        self._movies = []
        self._tickets = []
    
    def add_customer(self, customer):
        self._customers.append(customer)
        
    def add_movie(self, movie):
        self._movies.append(movie)
        
    def add_ticket(self, ticket):
        self._tickets.append(ticket)
        
    def get_customers(self):
        return self._customers
    
    def get_movies(self):
        return self._movies
    
    def get_tickets(self):
        return self._tickets

class Operations:
    def __init__(self):
        self._records = Records()

    def purchase_ticket(self):
        customer_id = input("Enter customer ID: ")
        customer = self.get_customer_by_id(customer_id)
        if customer is None:
            print("Customer not found.")
            return
        
        movie_id = input("Enter movie ID: ")
        movie = self.get_movie_by_id(movie_id)
        if movie is None:
            print("Movie not found.")
            return

        ticket_id = input("Enter ticket ID: ")
        ticket = self.get_ticket_by_id(ticket_id)
        if ticket is None:
            print("Ticket not found.")
            return

        if movie.update_seats_available(1):
            booking = Booking(customer, movie, ticket)
            print("Booking successful.")
            booking.display_info()
        else:
            print("Seats not available for the selected movie.")

    def get_customer_by_id(self, customer_id):
        for customer in self._records.get_customers():
            if customer.id == customer_id:
                return customer
        return None

    def get_movie_by_id(self, movie_id):
        for movie in self._records.get_movies():
            if movie.id == movie_id:
                return movie
        return None

    def get_ticket_by_id(self, ticket_id):
        for ticket in self._records.get_tickets():
            if ticket.id == ticket_id:
                return ticket
        return None

    def add_customer(self):
        customer_id = input("Enter customer ID: ")
        customer_name = input("Enter customer name: ")
        customer_type = input("Enter customer type (Standard/Reward Flat/Reward Step): ")

        if customer_type.lower() == "standard":
            customer = Customer(customer_id, customer_name)
        elif customer_type.lower() == "reward flat":
            discount_rate = float(input("Enter discount rate: "))
            customer = RewardFlatCustomer(customer_id, customer_name, discount_rate)
        elif customer_type.lower() == "reward step":
            discount_rate = float(input("Enter discount rate: "))
            threshold = float(input("Enter threshold: "))
            customer = RewardStepCustomer(customer_id, customer_name, discount_rate, threshold)
        else:
            print("Invalid customer type.")
            return

        self._records.add_customer(customer)
        print("Customer added successfully.")

    def add_movie(self):
        movie_id = input("Enter movie ID: ")
        movie_name = input("Enter movie name: ")
        seats_available = int(input("Enter number of seats available: "))

        movie = Movie(movie_id, movie_name, seats_available)
        self._records.add_movie(movie)
        print("Movie added successfully.")

    def add_ticket(self):
        ticket_id = input("Enter ticket ID: ")
        ticket_type = input("Enter ticket type: ")
        price = float(input("Enter ticket price: "))
        quantity = int(input("Enter ticket quantity: "))

        if quantity > 1:
            ticket = GroupTicket(ticket_id, ticket_type, price, quantity)
        else:
            ticket = Ticket(ticket_id, ticket_type, price)

        self._records.add_ticket(ticket)
        print("Ticket added successfully.")

    def display_records(self):
        print("Customers:")
        for customer in self._records.get_customers():
            customer.display_info()
        
        print("Movies:")
        for movie in self._records.get_movies():
            movie.display_info()
        
        print("Tickets:")
        for ticket in self._records.get_tickets():
            ticket.display_info()


def main():
    operations = Operations()
    while True:
        print("Select an option:")
        print("1. Purchase ticket")
        print("2. Add customer")
        print("3. Add movie")
        print("4. Add ticket")
        print("5. Display records")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            operations.purchase_ticket()
        elif choice == "2":
            operations.add_customer()
        elif choice == "3":
            operations.add_movie()
        elif choice == "4":
            operations.add_ticket()
        elif choice == "5":
            operations.display_records()
        elif choice == "6":
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()