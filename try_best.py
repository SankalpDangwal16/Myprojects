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
        
    def update_seats(self,booked_seats):
        self._seat_available -= booked_seats

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
        print(f"ID: {self._ticket_id}, ticket type: {self._ticket_type}, ticket price: {self._price}")

class GroupTicket(Ticket):
    def __init__(self, ticket_id, ticket_name, price, ticket_components):
        super().__init__(ticket_id, ticket_name, price)
        self._ticket_components = ticket_components
    
    def get_components(self):
        return self._ticket_components
         

class Booking:
    def __init__(self, customer:Customer, movie:Movie, ticket:Ticket, quantity:int)->None:
        self.customer = customer
        self.movie = movie
        self.ticket = ticket
        self.quantity = quantity

    def compute_cost(self):
        ticket_cost = self.ticket.get_price * self.quantity
        booking_fee = self.customer.get_booking_fee(self.quantity)
        discount = self.customer.get_discount(ticket_cost)
        return ticket_cost, booking_fee, discount

class Records:
    def __init__(self):
        self.customers = []
        self.movies = []
        self.tickets = []
        
    def generate_unique_id(self, prefix):
        ids = [int(customer.get_id[1:]) for customer in self.customers if customer.get_id.startswith(prefix)]
        if len(ids) == 0:
            return f"{prefix}1"
        else:
            new_id =  max(ids) + 1
            return f"{prefix}{new_id}"
        
    def add_customer(self, customer_name, reward_type="C"):
        if reward_type == "C":
            customer_id = self.generate_unique_id("C")
            customer = Customer(customer_id, customer_name)
        elif reward_type == "F":
            customer_id = self.generate_unique_id("F")
            customer = RewardFlatCustomer(customer_id, customer_name)
        elif reward_type == "S":
            customer_id = self.generate_unique_id("S")
            customer = RewardStepCustomer(customer_id, customer_name)
        else:
            raise ValueError("Invalid reward type.")
        self.customers.append(customer)
        return customer
        

    def read_customers(self, customer_filepath):
        customer_filepath = "C:/Users/sanka/OneDrive/Desktop/Programming Fundamentals/Assignment 2/COSC2531_Assignment2_txtfiles/New folder/customers.txt"
        #customer_filepath = os.path.join(self.folderpath,file_name)
        with open(customer_filepath, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                customer_id = data[0].strip()
                customer_name = data[1].strip()
                if customer_id.startswith('C'):
                    customer = Customer(customer_id,customer_name)
                elif customer_id.startswith('F'):
                    discount_rate = float(data[2].strip())
                    if discount_rate:
                        customer = RewardFlatCustomer(customer_id,customer_name,discount_rate)
                    else:
                        customer = RewardFlatCustomer(customer_id,customer_name)
                elif customer_id.startswith('S'):
                    discount_rate = float(data[2].strip())
                    threshold = float(data[3].strip())
                    if discount_rate and threshold:
                        customer = RewardStepCustomer(customer_id,customer_name,discount_rate, threshold)
                    elif discount_rate is not None and threshold is None:
                        customer = RewardStepCustomer(customer_id,customer_name,discount_rate=discount_rate)
                    elif threshold is not None and discount_rate is None:
                        customer = RewardStepCustomer(customer_id,customer_name,threshold=threshold)
                    else:
                        customer = RewardStepCustomer(customer_id,customer_name)
                        
                self.customers.append(customer)

    def read_movies(self, movie_filepath):
        movie_filepath = "C:/Users/sanka/OneDrive/Desktop/Programming Fundamentals/Assignment 2/COSC2531_Assignment2_txtfiles/New folder/movies.txt"
        # movie_filepath = os.path.join(self.folderpath,file_name)
        with open(movie_filepath, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                movie_id = data[0].strip()
                movie_name = data[1].strip()
                seat_available = int(data[2].strip())
                movie = Movie(movie_id, movie_name, seat_available)
                self.movies.append(movie)

    def read_tickets(self, ticket_filepath):
        ticket_filepath = "C:/Users/sanka/OneDrive/Desktop/Programming Fundamentals/Assignment 2/COSC2531_Assignment2_txtfiles/New folder/tickets.txt"
        # ticket_filepath = os.path.join(self.folderpath,file_name)
        with open(ticket_filepath, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                ticket_id = data[0].strip()
                ticket_name = data[1].strip()
                if ticket_id.startswith("G"):
                    components = {}
                    for i in range(2, len(data), 2):
                        ticket_type = self.find_ticket(data[i].strip())
                        quantity = int(data[i+1].strip())
                        components[ticket_type] = quantity
                    price = sum([ticket.get_price * quantity for ticket,quantity in components.items()])
                    if price >= 50:
                        ticket = GroupTicket(ticket_id, ticket_name, price,components)
                    else:
                        print(f"Something wrong with group ticket : ID:{ticket_id}, name: {ticket_name}")
                else:
                    ticket_price = float(data[2].strip())
                    ticket = Ticket(ticket_id, ticket_name, ticket_price)
                self.tickets.append(ticket)

    def find_customer(self, search_value):
        for customer in self.customers:
            if customer.get_id == search_value or customer.get_name == search_value:
                return customer
        return None
    
    def find_movie(self, search_value):
        for movie in self.movies:
            if movie.get_id == search_value or movie.get_name == search_value:
                return movie
        return None

    def find_ticket(self, search_value):
        for ticket in self.tickets:
            if ticket.get_id == search_value or ticket.get_type == search_value:
                return ticket
        return None

    def display_customers(self):
        for customer in self.customers:
            customer.display_info()

    def display_movies(self):
        for movie in self.movies:
            movie.display_info()

    def display_tickets(self):
        for ticket in self.tickets:
            ticket.display_info()
                 
        
class Operations:
    def __init__(self, records:Records):
        self.records = records

    def purchase_ticket(self):
        while True:
            try:
                # Get customer information
                customer_input = input("Enter customer name or id: ")
                customer = self.records.find_customer(customer_input)
                
                if customer:
                    print(customer.class_name())  # Print the customer's class name
                else:
                    while True:
                        if customer_input.isdigit():
                            print("Invalid name for a new customer. Please try again.")
                            customer_input = input("Enter customer name: ")
                        else:
                            break  # Exit the loop when valid customer name is entered
                
                if not customer:
                    while True:
                        reward_program_permission = input("Does the customer want to join the reward program [enter y or n]?")
                        if reward_program_permission not in ["n","y"]:
                            print("Invalid answer. Please enter y or n.")
                        elif reward_program_permission == "n":
                            customer = self.records.add_customer(customer_input)
                            print("Customer added successfully.")
                            break  # Exit the loop after customer is added
                        elif reward_program_permission == "y":
                            while True:
                                reward_type = input("What kind of rewards does the customer want? [F/S]")
                                if reward_type not in ["F", "S"]:
                                    print("Invalid rewards type. Please enter F or S.")
                                else:
                                    customer = self.records.add_customer(customer_input, reward_type)
                                    print("Customer added successfully to the rewards program.")
                                    break  # Exit the loop after customer is added
                            break
                            
                # Get movie information
                while True:
                    movie_input = input("Enter movie name: ")
                    movie = self.records.find_movie(movie_input)
                    if movie is None:
                        print("Invalid movie. Please try again.")
                    elif movie.get_seats == 0:
                        print("Sold out. Please try again.")
                    else:
                        break
    
                # Get ticket information
                while True:
                    ticket_input = input("Enter ticket name: ")
                    ticket = self.records.find_ticket(ticket_input)
                    if ticket is None:
                        print("Invalid ticket type. Please try again.")
                    else:
                        break
    
                # Get ticket quantity
                while True:
                    quantity_input = input("Enter ticket quantity: ")
                    if not quantity_input.isdigit() or int(quantity_input) <= 0:
                        print("Invalid quantity. Please try again.")
                    elif int(quantity_input) > movie.get_seats:
                        print("Quantity exceeds available seats. Please try again.")
                    else:
                        quantity = int(quantity_input)
                        break
    
                booking = Booking(customer, movie, ticket, quantity)
                ticket_cost, booking_fee, discount = booking.compute_cost()
    
                # Update available seats
                movie.update_seats(quantity)
    
                # Display receipt
                print("----------------")
                print(f"Receipt of {customer.get_name}")
                print("----------------")
                print(f"Movie: {movie.get_name}")
                print(f"Ticket type: {ticket.get_type}")
                print(f"Ticket unit price: {ticket.get_price}")
                print(f"Ticket quantity: {quantity}")
                print("----------------")
                print(f"Discount: {discount}")
                print(f"Booking fee: {booking_fee}")
                print(f"Total cost: {ticket_cost}")
                print("----------------")
    
                break
    
            except ValueError as e:
                print(f"Error: {str(e)}. Please try again.")

    

    def display_customers(self):
        self.records.display_customers()

    def display_movies(self):
        self.records.display_movies()

    def display_tickets(self):
        self.records.display_tickets()

    def exit_program(self):
        print("Exiting the program. Goodbye!")
        sys.exit(0)

    def run_menu(self):
        while True:
            print("----- Menu -----")
            print("1. Purchase a ticket")
            print("2. Display existing customers' information")
            print("3. Display existing movies' information")
            print("4. Display existing ticket types' information")
            print("5. Exit the program")

            choice = input("Enter your choice (1-5): ")
            print("----------------")

            if choice == "1":
                self.purchase_ticket()
            elif choice == "2":
                self.display_customers()
            elif choice == "3":
                self.display_movies()
            elif choice == "4":
                self.display_tickets()
            elif choice == "5":
                self.exit_program()
            else:
                print("Invalid choice. Please try again.")
            print("----------------")
            

    def display_customers(self):
        self.records.display_customers()

    def display_movies(self):
        self.records.display_movies()

    def display_tickets(self):
        self.records.display_tickets()

    def exit_program(self):
        print("Exiting the program. Goodbye!")
        sys.exit(0)

    def run_menu(self):
        while True:
            print("----- Menu -----")
            print("1. Purchase a ticket")
            print("2. Display existing customers' information")
            print("3. Display existing movies' information")
            print("4. Display existing ticket types' information")
            print("5. Exit the program")

            choice = input("Enter your choice (1-5): ")
            print("----------------")

            if choice == "1":
                self.purchase_ticket()
            elif choice == "2":
                self.display_customers()
            elif choice == "3":
                self.display_movies()
            elif choice == "4":
                self.display_tickets()
            elif choice == "5":
                self.exit_program()
            else:
                print("Invalid choice. Please try again.")
            print("----------------")

class Helper:
    
    @staticmethod
    def filepath(folderpath,filename):
        return os.path.join(folderpath, filename)
    
    @staticmethod
    def check_files_present(folderpath,files_to_check):
        missing_files = []
        for file_name in files_to_check:
            if not Helper.filepath(folderpath, file_name):
                missing_files.append(file_name)
        if len(missing_files) >0:
            raise FileNotFoundError("Following files cannot be found: {missing_files) in {folderpath).")

def main(folder_name):
    files_to_check = ["customers.txt", "movies.txt", "tickets.txt"]
    folderpath = Helper.filepath(os.getcwd(),folder_name)
    Helper.check_files_present(folderpath,files_to_check)
    customer_filepath = Helper.filepath(folderpath,files_to_check[0])
    movie_filepath = Helper.filepath(folderpath,files_to_check[1])
    ticket_filepath = Helper.filepath(folderpath,files_to_check[2])
    records = Records()
    records.read_customers(customer_filepath)
    records.read_movies(movie_filepath)
    records.read_tickets(ticket_filepath)
    operations = Operations(records)
    operations.run_menu()


if __name__ == "__main__":
    main("credit_level")