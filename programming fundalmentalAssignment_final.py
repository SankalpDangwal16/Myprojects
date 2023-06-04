# -*- coding: utf-8 -*-
"""
Created on Sat May  6 01:03:02 2023

@author: sanka
"""

#
#space 
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name 
     
    @property
    def get_name(self):
        return self.name
    
    @property
    def get_id(self):
        return self.customer_id
        
     
    def set_name(self, new_name):
        self.name = new_name
        
    def get_discount(self, cost):
        return 0
    
    def get_booking_fee(self, ticket_quantity):
        BOOKING_FEE = 2
        return BOOKING_FEE*ticket_quantity
    
    def display_info(self):
        print(f"customer_id:{self.customer_id}")
        print(f"name:{self.name}" )
        

class RewardFlatCustomer:
    def __init__(self,discount_rate=0.02):
        self.discount_rate = discount_rate
        
    @property        
    def get_discount_rate(self):
        return self.discount_rate
    
            
    def get_discount(self, cost):
        return  cost * self.discount_rate 
   
    def display_info(self):
        print(f"Discount rate:{self.discount_rate}")
        
    def set_discount_rate(self, new_discount_rate):
        self.discount_rate = new_discount_rate 


class RewardStepCustomer:
    def __init__(self, discount_rate=0.03,threshold=50):
        self.discount_rate = discount_rate
        self.threshold = threshold
        
    def get_discount_rate(self):
        return  self.discount_rate
    
    def get_threshold(self):
        return self.threshold
        
    def get_discount(self, cost):
        return cost * self.discount_rate
    
    def display_info(self):
        print(f"Discount Rate :{self.discount_rate}")
        print(f"Threshold:{self.threshold}")
        
    def set_discount_rate(self, new_discount_rate):
        self.discount_rate = new_discount_rate
        
    def set_threshold(self, new_threshold):
        self.threshold = new_threshold
        
class Movie:
    def __init__(self,ID, name, seat_available):
        self.ID = ID
        self.name = name
        self.seat_available = seat_available
        
    def display_info(self):
        print(f"ID: {self.ID}")
        print(f"Movie name:{self.name}")    
        print(f"Available Seats:{self.seat_available}")
        
class Ticket:
    def __init__(self,ID, name,price):
        self.ID = ID
        self.name = name
        self.price = price
        
    def display_info(self):
        print(f"ID: {self.ID}")
        print(f"Ticket type:{self.name}")    
        print(f"Ticket price:{self.price}") 
        

class Booking:
    
    def __init__(self, customer, movie, ticket, quantity):
        self.customer = customer
        self.movie = movie
        self.ticket = ticket
        self.quantity = quantity
        
    def compute_cost(self, ticket_cost, booking_fee, discount_cost):
        return ticket_cost,booking_fee,discount_cost
    

                
class Records:
    def __init__(self):
        customer_file_path = "C:/Users/sanka/OneDrive/Desktop/Programming Fundamentals/Assignment 2/COSC2531_Assignment2_txtfiles/pass_level/customers.txt" 
        movies_path = "C:/Users/sanka/OneDrive/Desktop/Programming Fundamentals/Assignment 2/COSC2531_Assignment2_txtfiles/pass_level/movies.txt"     
        tickets_path = "C:/Users/sanka/OneDrive/Desktop/Programming Fundamentals/Assignment 2/COSC2531_Assignment2_txtfiles/pass_level/tickets.txt"   
        
        self.customers = []
        self.movies = []
        self.tickets = []

    def read_customers(self, filename):
        with open("C:/Users/sanka/OneDrive/Desktop/Programming Fundamentals/Assignment 2/COSC2531_Assignment2_txtfiles/pass_level/customers.txt", 'r') as file:
            for line in file:
                data = line.strip().split(',')
                ID = data[0].strip()
                name = data[1].strip()
                if ID.startswith('C'):
                    customer = Customer(ID, name)
                elif ID.startswith('F'):
                    discount_rate = float(data[2].strip())
                    customer = RewardFlatCustomer(ID, name, discount_rate)
                elif ID.startswith('S'):
                    discount_rate = float(data[2].strip())
                    threshold = float(data[3].strip())
                    customer = RewardStepCustomer(ID, name, discount_rate)
                    RewardStepCustomer.set_threshold(threshold)
                self.customers.append(customer)
        

    def read_movies(self, filename):
        with open("C:/Users/sanka/OneDrive/Desktop/Programming Fundamentals/Assignment 2/COSC2531_Assignment2_txtfiles/pass_level/movies.txt", 'r') as file:
            for line in file:
                data = line.strip().split(',')
                ID = data[0].strip()
                name = data[1].strip()
                seats_available = int(data[2].strip())
                
                if not ID.startswith('M'):
                        continue
                movie = Movie(ID, name, seats_available)
                self.movies.append(movie)

    def read_tickets(self, filename):
        with open("C:/Users/sanka/OneDrive/Desktop/Programming Fundamentals/Assignment 2/COSC2531_Assignment2_txtfiles/pass_level/tickets.txt", 'r') as file:
            for line in file:
                print(line)
                data = line.strip().split(',')
                ID = data[0].strip()
                name = data[1].strip()
                price = float(data[2].strip())
                ticket = Ticket(ID, name, price)
                self.tickets.append(ticket)

    def find_customer(self, search_value):
        for customer in self.customers:
            if search_value == customer.ID or search_value == customer.name:
                return customer
        return None

    def find_movie(self, search_value):
        for movie in self.movies:
            if search_value == movie.ID or search_value == movie.name:
                return movie
        return None

    def find_ticket(self, search_value):
        for ticket in self.tickets:
            if search_value == ticket.ID or search_value == ticket.name:
                return ticket
        return None

    def display_customers(self):
        print("Existing Customers:")
        for customer in self.customers:
            customer.display_info()
            if isinstance(customer, RewardFlatCustomer) or isinstance(customer, RewardStepCustomer):
                print("Discount Rate:", customer.get_discount_rate())
            if isinstance(customer, RewardStepCustomer):
                print("Threshold:", customer.threshold)
            print()

    def display_movies(self):
        print("Available Movies:")
        for movie in self.movies:
            movie.display_info()
            print("Seats Available:", movie.seat_available)
            print()

    def display_tickets(self):
        print("Available Ticket Types:")
        for ticket_type in self.ticket_types:
           ticket_type.display_info()
           print("Unit Price:", ticket_type.price)
           print()   
                      

class Operations:
    def __init__(self):
        self.records = Records()  # Create an instance of the Records class

    def start(self):
        self.load_data()  # Load data from files
        self.display_menu()  # Display the menu options

    def load_data(self):
        try:
            self.records.read_customers("customers.txt")                         # Read customer data from file
            self.records.read_movies("movies.txt")                               # Read movie data from file
            self.records.read_tickets("tickets.txt")                             # Read ticket data from file
        except FileNotFoundError as e:
            print(f"Error: {e.filename} not found. Exiting the program.")
            exit()

    def display_menu(self):
        while True:
            print("Menu:")
            print("1. Purchase a ticket")
            print("2. Display existing customers' information")
            print("3. Display existing movies' information")
            print("4. Display existing ticket types' information")
            print("5. Exit the program")

            choice = input("Enter your choice (1-5): ")
            print()

            if choice == "1":
                self.purchase_ticket()
            elif choice == "2":
                self.records.display_customers()
            elif choice == "3":
                self.records.display_movies()
            elif choice == "4":
                self.records.display_tickets()
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
            print()
            
    def purchase_ticket(self):
        customer_id = input("Enter customer ID: ")
        customer = self.records.find_customer(customer_id)

        if customer is None:
            customer_name = input("Enter customer name: ")
            rewards_program = self.get_valid_input("Register for rewards program? (y/n): ", ["y", "n"])
        
            if rewards_program.lower() == "y":
                rewards_type = self.get_valid_input("Enter rewards type (F/S): ", ["F", "S"])
                if rewards_type.upper() == "F":
                    customer = RewardFlatCustomer(customer_id, customer_name)
                elif rewards_type.upper() == "S":
                    customer = RewardStepCustomer(customer_id, customer_name)
            else:
                customer = Customer(customer_id, customer_name)
            self.records.customers.append(customer)
            
        else:
            print("Existing customer:")
            customer.display_info()

        while True:
           movie_id = input("Enter movie ID: ")
           movie = self.records.find_movie(movie_id)

           if movie is None:
               print("Invalid movie ID. Please try again.")
               continue
           elif movie.seats_available == 0:
               print("Movie is sold out. Please choose another movie.")
               continue
           break

        while True:
           ticket_id = input("Enter ticket type ID: ")
           ticket_type = self.records.find_ticket(ticket_id)

           if ticket_type is None:
               print("Invalid ticket type ID. Please try again.")
               continue
           break
   
    
        while True:
           try:
               ticket_quantity = int(input("Enter ticket quantity: "))
               if ticket_quantity <= 0:
                   raise ValueError("Ticket quantity must be a positive integer.")
               if ticket_quantity > movie.seats_available:
                   raise ValueError("Ticket quantity exceeds available seats.")
               break
           except ValueError as e:
               print(f"Invalid input: {e}. Please try again.")

        booking = Booking(customer, movie, ticket_type, ticket_quantity)
        ticket_cost, booking_fee, discount = booking.compute_cost()
       
        if isinstance(ticket_type, GroupTicketType):
           min_price = ticket_quantity * 50.0
           group_ticket_price = max(ticket_cost * 0.8, min_price)
           ticket_cost = group_ticket_price
    
        total_cost = ticket_cost + booking_fee - discount
    
        print("------------------------------------------------------------------------------")
        print(f"Receipt of {customer.get_name()}")
        print("------------------------------------------------------------------------------")
        print(f"Movie: {movie.name}")
        print(f"Ticket type: {ticket_type.name}")
        print(f"Ticket unit price: {ticket_type.price}")
        print(f"Ticket quantity: {ticket_quantity}")
        print("------------------------------------------------------------------------------")
        print(f"Discount: {discount}")
        print(f"Booking fee: {booking_fee}")
        print(f"Total cost: {total_cost}")
        print("------------------------------------------------------------------------------")

    def get_valid_input(self, prompt, valid_options):
        while True:
            user_input = input(prompt)
            if user_input in valid_options:
                return user_input
            print("Invalid input. Please try again.")