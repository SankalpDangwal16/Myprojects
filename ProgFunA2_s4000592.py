import sys

# Student Name : Sankalp Dangwal
# Student ID   : s4000592
# Highest part Attempted : HD (Completed)
# This code is error free and meets all the expectations

# Analysis

#----------------------------------------------------------------------------------------------------------

# Each programme component has been developed using an object-oriented paradigm, and The programme is divided into objects, each of which has its own methods and attributes.
# Access modifiers are frequently used to prevent unintended changes to object.
# Getters and setters were implemented for each object to make it easier to access object variables. 
# The inheritance is used whenever possible makes advantage of object-oriented capabilities, has reduced the amount of code.
# This feature's implementation in part 1 had a number of issues, including the inability to test the code as classes, variables, and methods were initializing. .
# Several little and significant bugs needed to be repaired.
# The first component (pass level) was simpler to manage and implement. Additionally, there were no invalid input values. 
# However, the initialisation procedure took a lot of time and work. The requirements for the credit level 
# were somewhat less convoluted, but still challenging, so I was obliged to use custom exceptions rather than while  loops to assure precise entry. 
# To get the desired outcome, I combined recursion with exception handling.
# The introduction of group tickets significantly increased the complexity of the programme and needed the creation of logic to handle such cases because one ticket could now fill more than 1 seat.
# Since I didn't know how many values would be contained in each line of the # text files, reading the group tickets from those files proved to be challenging.
# We found it easier to implement these requirements because we could always count on there being valid input. At the DI level, the requirement to accept multiple inputs was introduced. 
# Because object-oriented programmes adhere to the concept of modularity, 
# it was easier to meet the requirements because changes could be made to a specific area of the programme without running the risk of the programme crashing altogether. 
# Due to the fact that each ticket transaction will be included in a single booking, the Booking object had to be changed.
# The pass-level included the implementation of the techniques to modify the discount rates for the clients.
# Additionally, a means to retrieve client information was implemented. To correctly invoke those # methods, I just had to implement a method. 
# I had to read the booking information and preload the booking object as requested by HD.
# Reading the booking information was difficult, but applying the logic to read the group ticket information had given me a clue as to how to read an arbitrary number of comma-separated data. 
# It was simple to display all the booking details because a booking object would store all the information, including the movie and ticket details.
# In order to handle scenarios where the amount of arguments provided was incorrect and others, accepting command line arguments required a few minor tweaks to the program's initialisation phase. 
# Given that formatting data and accurately displaying them was required in the initial assignments, I strengthened my talents and was able to use string formatting  efficiently to display all the movie records.

#----------------------------------------------------------------------------------------------------------------------------------------------

#This class is used to keep track of each customer's fundamental information.
class Customer:
    
    def __init__(self, ID, name):
        self.__ID = ID
        self.__name = name

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self,value):
        self.__ID = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    def get_discount(self, cost):
        return 0

    def get_booking_fee(self, ticket_quantity):
        return 2 * int(ticket_quantity)

    def display_info(self):
        print("Customer ID: " + self.__ID)
        print("Customer name: " + self.__name)
#------------------------------------------------------------------------------------------------------------------------------

#This class is used to keep track of each RewardFlat customer's information.
class RewardFlatCustomer(Customer):
    
    __discount_rate = 0.2

    @staticmethod
    def get_discount_rate():
        return float(RewardFlatCustomer.__discount_rate)
    
    @staticmethod
    def set_discount_rate(new_discount_rate):
        RewardFlatCustomer.__discount_rate = new_discount_rate

    @staticmethod
    def get_discount(cost):
        return round(RewardFlatCustomer.get_discount_rate() * float(cost), 2)

    def display_info(self):
        print("Customer ID: " + self.ID)
        print("Customer name: " + self.name)
        print("Discount rate: " + str(RewardFlatCustomer.__discount_rate))

#-----------------------------------------------------------------------------------------------------------------------------

# The details of each individual RewardStep customer are kept in this class.
class RewardStepCustomer(Customer):

    __discount_rate = 0.3
    __threshold = 50

    def __init__(self, ID, name, discount_rate, threshold):
        super().__init__(ID, name)
        if discount_rate == -1:
            self.__discount_rate = RewardStepCustomer.get_default_discount_rate()  
        else:
            self.__discount_rate = discount_rate
        if threshold != RewardStepCustomer.get_threshold():
            RewardStepCustomer.set_threshold(threshold)
    
    @staticmethod
    def get_threshold():
        return int(RewardStepCustomer.__threshold)
    
    @staticmethod
    def get_default_discount_rate():
        return float(RewardStepCustomer.__discount_rate)

    @property
    def discount_rate(self):
        return float(self.__discount_rate)

    @discount_rate.setter
    def discount_rate(self, new_discount_rate):
        self.__discount_rate =  new_discount_rate

    @staticmethod
    def set_threshold(new_threshold):
        RewardStepCustomer.__threshold = new_threshold

    def get_discount(self, cost):
        if cost >= RewardStepCustomer.get_threshold():
            return round(cost * self.discount_rate, 2)
        else:
            return 0
    
    def display_info(self):
        print("Customer ID: " + self.ID)
        print("Customer name: " + self.name)
        print("Discount rate: " + str(self.discount_rate))
        print("Discount threshold: " + str(RewardStepCustomer.get_threshold()))

#------------------------------------------------------------------------------------------

#This class serves as a repository for each movie detail.
class Movie:
    def __init__(self, ID, name, seat_available):
        self.__ID = ID
        self.__name = name
        self.__seat_available = int(seat_available)
        self.__revenue = 0

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self,value):
        self.__ID = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def seat_available(self):
        return self.__seat_available
    
    @seat_available.setter
    def seat_available(self,value):
        self.__seat_available =  value
    
    @property
    def revenue(self):
        return self.__revenue
    
    @revenue.setter
    def revenue(self,value):
        self.__revenue =  value

    def display_info(self):
        print(self.ID.ljust(23," ")+self.name.ljust(23," ")+ str(int(self.seat_available)).ljust(23," "))

#------------------------------------------------------------------------------------------

#The information for each ticket is kept in this class.
class Ticket:
    def __init__(self, ID, name, price):
        self.__ID = ID
        self.__name = name
        self.__price = float(price)

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self,value):
        self.__ID = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def price(self):
        return float(self.__price)
    
    @price.setter
    def price(self,value):
        self.__price =  float(value)

    def display_info(self):
        print(self.ID.ljust(23," ")+self.name.ljust(23," ")+ str(self.price))

#------------------------------------------------------------------------------------------

#The information for each group ticket is kept in this class[Child of Ticket]
class GroupTicket(Ticket):

    def __init__(self, ID, name, ticket_list, quantity_list, price):
        super().__init__(ID, name, float(price))
        self.__ticket_list = ticket_list
        self.__quantity_list = quantity_list
    
    @property
    def ticket_list(self):
        return self.__ticket_list
    
    @ticket_list.setter
    def ticket_list(self,value):
        self.__ticket_list =  value

    @property
    def quantity_list(self):
        return self.__quantity_list
    
    @quantity_list.setter
    def quantity_list(self,value):
        self.__quantity_list =  value

    def display_info(self):
        print(self.ID.ljust(23," ")+self.name.ljust(23," ")+ str(self.price))

#------------------------------------------------------------------------------------------

#This class keeps track of all reservations. Each booking is recorded as an object, and each booking object is linked to the customer, 
#movie, and ticket objects # connected with the booking.
class Booking:

    def __init__(self, customer, movie, tickets, quantities, discount, booking_fee, total_ticket_cost):
        self.__customer = customer
        self.__movie = movie
        self.__ticket_list = tickets
        self.__quantity_list = quantities
        self.__total_ticket_cost = total_ticket_cost
        self.__booking_fee = booking_fee
        self.__discount = discount
    
    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self,value):
        self.__customer = value
    
    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self,value):
        self.__movie = value

    @property
    def ticket_list(self):
        return self.__ticket_list

    @ticket_list.setter
    def ticket_list(self,value):
        self.__ticket_list = value

    @property
    def quantity_list(self):
        return self.__quantity_list

    @quantity_list.setter
    def quantity_list(self,value):
        self.__quantity_list = value

    @property
    def total_ticket_cost(self):
        return self.__total_ticket_cost

    @total_ticket_cost.setter
    def total_ticket_cost(self,value):
        self.__total_ticket_cost = value

    @property
    def booking_fee(self):
        return self.__booking_fee

    @booking_fee.setter
    def booking_fee(self,value):
        self.__booking_fee = value

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self,value):
        self.__discount = value

    #This process calculates each booking's cost. The booking object supplied to this method had all the information required to
    #total the costs. I can determine whether to apply a discount based on the consumer information. The film explains which seats need to be modified.
    #The ticket type and the number of each ticket are stored on the two lists. Together, they work well enough to process the data. 
    #and determine the price for this specific reservation. This procedure provides the booking charge, overall ticket price, and any applicable discount.
    def compute_cost(self):
        
        #basic ticket cost
        total_quantities = 0
        for i in range(len(self.ticket_list)):
            ticket_cost = float(self.ticket_list[i].price) * int(self.quantity_list[i])
            total_quantities += self.quantity_list[i]
            self.total_ticket_cost += ticket_cost
        
        #discount based on customer
        if isinstance(self.customer, RewardFlatCustomer):
            self.discount = self.customer.get_discount(self.total_ticket_cost)
        elif isinstance(self.customer, RewardStepCustomer):
            if self.total_ticket_cost >= RewardStepCustomer.get_threshold():
                self.discount = self.customer.get_discount(self.total_ticket_cost)

        # Compute the booking fee
        self.booking_fee = self.customer.get_booking_fee(total_quantities)

        return self.total_ticket_cost, self.booking_fee, self.discount
    
    #This function is triggered each time a successful reservation is made to update the number of seats still available.
    def update_ticket_quantity(self):
        totaltickets = 0 
        for i in range(len(self.__ticket_list)):
            if isinstance(self.__ticket_list[i],GroupTicket):
                sum = 0
                for quantity in self.__ticket_list[i].quantity_list:
                    sum = sum + quantity
                totaltickets += self.__quantity_list[i]*sum
            else:
                totaltickets += self.__quantity_list[i]
        self.__movie.seat_available = self.__movie.seat_available - totaltickets

#-------------------------------------------------------------------------------------------------------------------------------


#Every single current client, movie, ticket, and booking is kept in this class, which serves as the central data repository.
class Records:

    __customer_list = []
    __movie_list = []
    __ticket_list = []
    __group_ticket_list = []
    __booking_list = []

    @staticmethod
    def get_customer_list():
        return Records.__customer_list
    
    @staticmethod
    def get_movie_list():
        return Records.__movie_list

    @staticmethod
    def get_ticket_list():
        return Records.__ticket_list
    
    @staticmethod
    def get_group_ticket_list():
        return Records.__group_ticket_list
    
    @staticmethod
    def get_group_ticket_list():
        return Records.__group_ticket_list
    
    @staticmethod
    def get_booking_list():
        return Records.__booking_list

    @staticmethod
    def add_customer(customer):
        Records.get_customer_list().append(customer)

#------------------------------------------------------------------------------------------

#This is done to make unique exceptions that display unique messages.
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

#----------------------------------------------------------------------------------------------------------

#The code defines the __init__ method, which serves as the constructor for the Operations class. 
#It is responsible for reading command line arguments and performing appropriate actions based on the provided arguments. 
#The comments explain the purpose and functionality of each section of the code, including error handling for incorrect argument counts and calling methods to read files based on the arguments.
class Operations:

    def __init__(self):
        
        #Read the input from the command line arguments and if no command line arguments are specified, then read default files. 
        if len(sys.argv) == 2 or len(sys.argv) == 3 or len(sys.argv) > 5:
            print("Please enter either 3, 4 or 0 arguements for this program")
            print("Argument 1 will read the customer details from the text file specified in the arugment ")
            print("Argument 2 will read the movie details from the text file specified in the arugment ")
            print("Argument 3 will read the ticket details from the text file specified in the arugment ")
            print("If providing Argument 4, it will read the booking details from the text file specified in the arugment ")
            print("Try running the program again")
            print("Thank you")
            sys.exit()


        if len(sys.argv) >1:
            Operations.read_customers(sys.argv[1])
            Operations.read_movies(sys.argv[2])
            Operations.read_ticket(sys.argv[3])
            if len(sys.argv) == 5:
                Operations.read_booking(sys.argv[4])
        else:
            Operations.read_customers("customers.txt")
            Operations.read_movies("movies.txt")
            Operations.read_ticket("tickets.txt")
            Operations.read_booking("bookings.txt")

        #The Menu. This is repeated using a while loop so that every 
        while True:
            print("\n\nWelcome to the RMIT movie ticketing system!")
            print("######################################################")
            print("You can choose from the following options:\n 1. Purchase a ticket\n 2. Display existing customer informaton")
            print(" 3. Display exisiting movie information\n 4. Display Existing ticket information\n 5. Add movies")
            print(" 6. Adjust discount rate of all RewardFlat customers\n 7. Adjust the discount rate of a RewardStep customer")
            print(" 8. Display all bookings\n 9. Display the most popular movie")
            print("10. Display all bookings\n 0. Exit")
            print("######################################################")
            option = input("Choose one option\n")
            if not option.isdigit():
                print("ERROR : Incorrect Choice")
                continue
            option = int(option)
            if(option == 1):
                self.purchase_ticket()
            elif(option == 2):
                Operations.display_customer()
            elif(option == 3):
                Operations.loadMovieRevenue()
                Operations.display_movies()
                Operations.clearRevenue()
            elif(option == 4):
                Operations.display_tickets()
            elif(option == 5):
                Operations.addMovies()
            elif(option == 6):
                Operations.updateDiscountRewardFlat()
            elif(option == 7):
                Operations.updateDiscountRewardStep()  
            elif(option == 8):
                Operations.display_bookings()
            elif(option == 9):
                Operations.loadMovieRevenue()
                Operations.displayMaxRevenue()
                Operations.clearRevenue()
            elif(option == 10):
                Operations.loadMovieRevenue()
                Operations.displayAllMovieRecords()
                Operations.clearRevenue()
            elif(option == 0):
                #Writing back the processed information to the text files 
                if len(sys.argv) >1:
                    Operations.write_customer(sys.argv[1])
                    Operations.write_movie(sys.argv[2])
                    if len(sys.argv) == 5:
                        Operations.write_booking(sys.argv[4])
                    else:
                        Operations.write_booking("bookings.txt")
                else:
                    Operations.write_customer("customers.txt")
                    Operations.write_movie("movies.txt")
                    Operations.write_booking("bookings.txt")
                print("thank you")
                break
            else:
                print("ERROR : Incorrect Choice")
    
    #This method carries out the necessary steps for buying a ticket.
    @staticmethod
    def purchase_ticket():

        customer_search_value = input("Please enter your ID / name\n").strip()
        customer = Operations.find_customer(customer_search_value)
        movie = Operations.input_movie()
        tickets = Operations.input_ticket()
        quantities = Operations.input_Quantity(movie, tickets)

         #This line of code is used to create a new client account.
        if customer is None:
            customer_id_generation_code_part_2 = len(Records.get_customer_list())
            print("There are no previous records of the given customer details.\nInitiating registration process...")
            customer_name = input("Please enter your name\n")
            answer = Operations.input_enrollment()
            if answer == "y":
                choice = Operations.input_choice()
                if choice == "F":
                    customer_id = choice + str(customer_id_generation_code_part_2)
                    while isinstance(Operations.find_customer(customer_id),Customer):
                        customer_id_generation_code_part_2 += 1
                        customer_id = choice + str(customer_id_generation_code_part_2)
                    customer = RewardFlatCustomer(customer_id, customer_name)
                    Records.add_customer(customer)
                if choice == "S":
                    customer_id = choice + str(customer_id_generation_code_part_2)
                    while isinstance(Operations.find_customer(customer_id),Customer):
                        customer_id_generation_code_part_2 += 1
                        customer_id = choice + str(customer_id_generation_code_part_2)
                    customer = RewardStepCustomer(customer_id, customer_name, -1, 50)
                    Records.add_customer(customer)
            else:
                customer_id = "C" + str(customer_id_generation_code_part_2)
                customer = Customer(customer_id, customer_name)
                Records.add_customer(customer)

        #Here, the booking object is built using the supplied data, and the booking fee is computed.
        booking  = Booking(customer, movie, tickets, quantities, 0, 0, 0)
        ticket_cost, booking_fee, discount = booking.compute_cost()
        booking.update_ticket_quantity()
        Records.get_booking_list().append(booking)

        total_cost = float(ticket_cost) + float(booking_fee) - float(discount)
        #Printing th receipt     
        print("\n \n")
        print('-----------------------------------------------------------------------')
        print('Receipt of ' + customer.name)
        print('-----------------------------------------------------------------------')
        paddingMax = len("-----------------------------------------------------------------------")
        Operations.printReceipt("Movie:", movie.name , paddingMax)
        for i in range(len(tickets)):
            Operations.printReceipt("Ticket type:", tickets[i].name, paddingMax)
            Operations.printReceipt("Ticket unit price:", str(tickets[i].price), paddingMax)
            Operations.printReceipt("Ticket quantity:", str(quantities[i]), paddingMax)
            if not (i+1 == len(tickets)):
                print("                        --------------------")
        print('-----------------------------------------------------------------------')
        Operations.printReceipt("Discount:", str(round(discount,2)), paddingMax)
        Operations.printReceipt("Booking fee:", str(round(booking_fee,2)), paddingMax)
        Operations.printReceipt("Total cost:", str(round(total_cost,2)), paddingMax)

    #Discount rate of RewardFlat customer is updated using this method.
    @staticmethod
    def updateDiscountRewardFlat():
        try:
            discount = float(input("Please enter the new discount rate for RewardFlat customer [Any value greater than 0.0 and less than or equal to 1.0] \n"))
            if float(discount) <= 0.0 or float(discount) > 1.0: 
                    raise CustomException("Invalid discount rate")
        except CustomException as e:
            print(e.message)
            Operations.updateDiscountRewardFlat()
        except ValueError:
            print("Incorrect value entered. Please try again \n")
            Operations.updateDiscountRewardFlat()
        else:
            RewardFlatCustomer.set_discount_rate(discount)
            print("The discount rate for reward flat customers has been updated to "+ str(discount))   

    #This method is used to update the discount rate of RewardStep customer
    @staticmethod
    def updateDiscountRewardStep():
        try:
            customer_search_value = input("Please enter the reward step customer ID / name\n").strip()
            customer = Operations.find_customer(customer_search_value)
            if customer is None:
                raise CustomException("Invalid Customer ID")
            discount = float(input("Please enter the new discount rate for this reward step customer [Any value greater than 0.0 and less than or equal to 1.0] \n"))
            if float(discount) <= 0 or float(discount) > 1: 
                raise CustomException("Invalid discount rate")
        except CustomException as e:
            print(e.message)
            Operations.updateDiscountRewardStep()
        except ValueError:
            print("Incorrect value entered. Please try again \n")
            Operations.updateDiscountRewardStep()
        else:
            customer.discount_rate =  discount
            print("The discount rate for reward step customers has been updated to "+ str(discount)) 

#The methods whose names start with "input_value" are recursive methods.
#This means that if an invalid value is entered, these methods will automatically invoke and ask the user to provide the correct data.

    #Method to get the Movie details
    @staticmethod
    def input_movie():
        try:
            movie_search_value = input("Please enter the movie ID / name\n").strip()
            movie = Operations.find_movie(movie_search_value)
            if not movie: 
                raise CustomException("Invalid movie name/ID")
            if movie.seat_available == 0:
                raise CustomException("No seats available for this movie")
        except CustomException as e:
            print(e.message)
            movie = Operations.input_movie()
        else:
            return movie
        finally:
            return movie

    #Method to get the ticket details. Note that in this method, the input value is given in the form of comma sepearated values
    @staticmethod
    def input_ticket():
        tickets = []
        try:
            ticketTypes = [(x.strip()) for x in input("Please enter the list of ticket types\n").split(',')]
            for ticket_search_value in ticketTypes: 
                ticket = Operations.find_ticket(ticket_search_value)
                if not ticket: 
                    raise CustomException("Invalid ticket name/ID")
                else :
                    tickets.append(ticket)  
        except CustomException as e:
            print(e.message)
            tickets = Operations.input_ticket()
        else:
            return tickets
        finally:
            return tickets

    #Method for obtaining quantity information. This approach requires comma-separated values as input values.
    #In order to confirm that the necessary number of seats are available, each input is also double-checked with the movie. 
    #Note that the number of seats are not deducted here but the cummulative number of seats is recorded for verification
    @staticmethod
    def input_Quantity(movie, tickets):
        try:
            ticketQuantities = [int(x.strip()) for x in input("Please enter the list of ticket quantities\n").split(',')]
            if len(ticketQuantities) != len(tickets):
                raise CustomException("ERROR : The entries of ticket quantities do not match the entry of ticket types")
            check_value = 0
            for i in range(len(ticketQuantities)):
                check_value += int(ticketQuantities[i])
                if  ticketQuantities[i] <= 0 or ticketQuantities[i] >50: 
                    raise CustomException("Invalid ticket Quantity")
                if isinstance(tickets[i],GroupTicket):
                    sum = 0
                    for quantity in tickets[i].quantity_list:
                        sum = sum + quantity
                    check_value += int(ticketQuantities[i]) * sum    
                if int(check_value) > movie.seat_available:
                    raise CustomException("Ticket quantity exceeds total number of seats available")
        except CustomException as e:
            print(e.message)
            ticketQuantities = Operations.input_Quantity(movie, tickets)
        except ValueError:
            print("Incorrect value entered. Please try again \n")
            ticketQuantities = Operations.input_Quantity(movie, tickets)
        else:
            return ticketQuantities
        finally:
            return ticketQuantities

    #Method to get the customer's enrollment decision
    @staticmethod
    def input_enrollment():
        try:
            answer = input("Do you wish to enroll for the rewards program?\n").lower()
            possibleValues = ['y','n','Y','N']
            if answer not in possibleValues:
                raise CustomException("Invalid input. Please enter (Y/N)")
        except CustomException as e:
            print(e.message)
            answer = Operations.input_enrollment()
        else:
            return answer
        finally:
            return answer

    #Method to get the customer's enrollment choice
    @staticmethod
    def input_choice():
        try:
            choice = input("Choose your reward type\nFor RewardFlat press F\nFor RewardStep press S\n")
            possibleValues = ['F','S']
            if choice not in possibleValues:
                raise CustomException("Invalid input. Please enter (F/S)")
        except CustomException as e:
            print(e.message)
            choice = Operations.input_choice()
        else:
            return choice
        finally:
            return choice
    
    #This method reads the customer details from the specified file name given in the method argument
    @staticmethod
    def read_customers(file_name):
        try:
            file_name = "C:/Users/sanka/OneDrive/Desktop/Programming Fundamentals/Assignment 2/COSC2531_Assignment2_txtfiles/credit_level/customers.txt"
            text_file = open(file_name,'r')
            lines = text_file.readlines()
            for line in lines:
                inputList = [(x.strip()) for x in line.split(',')]
                customerType = inputList[0][0]
                if  customerType == "C":
                    customer = Customer(inputList[0], inputList[1])
                    Records.add_customer(customer)
                elif customerType == "F":
                    customer = RewardFlatCustomer(inputList[0], inputList[1])
                    if inputList[2] !=  RewardFlatCustomer.get_discount_rate():
                        customer.set_discount_rate(inputList[2])
                    Records.add_customer(customer)
                elif customerType == "S":
                    customer = RewardStepCustomer(inputList[0], inputList[1],inputList[2], inputList[3])
                    Records.add_customer(customer)
                else:
                    print("ERROR : Cannot load the customers file details successfully \nExiting program...")
                    sys.exit()
        except Exception as e:
            print("ERROR : Cannot load the customers file details successfully \nExiting program...")
            sys.exit()
        
    #This method reads the movie details from the specified file name given in the method argument
    @staticmethod
    def read_movies(file_name):
        try:
            text_file = open(file_name,'r')
            lines = text_file.readlines()
            for line in lines:
                try:
                    inputList = [(x.strip()) for x in line.split(',')]
                    movie = Movie(inputList[0], inputList[1], inputList[2])
                    Records.get_movie_list().append(movie)
                except:
                    print("ERROR : Cannot load the movies file details successfully \nExiting program...")
                    sys.exit()
        except Exception as e:
            print("ERROR : Cannot load the movies file details successfully \nExiting program...")
            sys.exit()

    # This method reads the ticket details from the specified file name given in the method argument.It is assumed that 
    # the files have correct and relevant data. The logic to make sure that the group tickets prices are above 50$ is added
    # If the calculated price of the group ticket is less than 50$ then it is ignored.
    def read_ticket(file_name):
        try:
            text_file = open(file_name,'r')
            lines = text_file.readlines()
            for line in lines:
                inputList = [(x.strip()) for x in line.split(',')]
                if inputList[0][0] == 'T' :
                    ticket =  Ticket(inputList[0], inputList[1], inputList[2])
                    Records.get_ticket_list().append(ticket)
                elif inputList[0][0] == 'G' :
                    group_ticket_id = inputList[0]
                    group_ticket_name = inputList[1]
                    group_ticket_list = []
                    group_ticket_quantity_list = []
                    #Here i delete the first two elements of the inputList as I have already recorded them
                    del inputList[:2]   
                    for i in range(0, len(inputList), 2):
                        group_ticket_list.append(inputList[i])
                        group_ticket_quantity_list.append(float(inputList[i+1]))
                    price = Operations.get_group_ticket_price(group_ticket_list,group_ticket_quantity_list)
                    if price >= 50:
                        group_ticket = GroupTicket(group_ticket_id, group_ticket_name, group_ticket_list, group_ticket_quantity_list, price)
                        Records.get_group_ticket_list().append(group_ticket)
                    else: 
                        print("ERROR : Invalid group ticket " + str(group_ticket_id)+", The price of group ticket needs to be equal to or higher than 50$  Action : Ticket entry ignored ")  
                            
        except Exception as e:
            print("ERROR :Cannot load the tickets file details successfully \nExiting program...")
            sys.exit()
    # This method reads the booking details from the specified file name given in the method argument.                
    @staticmethod
    def read_booking(file_name):
        try:
            text_file = open(file_name,'r')
        except Exception as e:
            print("Cannot load the booking file, running as if there is no previous booking file")
        else:       
            lines = text_file.readlines()
            try:    
                for line in lines:
                    inputList = [(x.strip()) for x in line.split(',')]
                    customer = Operations.find_customer(inputList[0])
                    movie = Operations.find_movie(inputList[1])
                    total_cost = float(inputList[-1])
                    booking_fee = float(inputList[-2])
                    discount = float(inputList[-3])
                    #The first two and the last 3 elements of the inputList are deleted after they are recorded
                    del inputList[:2]
                    del inputList[-3:]  
                    tickets = []
                    quantities = []
                    #The itterator jumps 2 numbers because each ticket has its corresponding quantitiy specified next to it 
                    for i in range(0, len(inputList), 2):
                        ticket = Operations.find_ticket(inputList[i])
                        tickets.append(ticket)
                        quantities.append(int(inputList[i+1]))
                    #Create booking object with the given details
                    booking  = Booking(customer, movie, tickets, quantities, discount, booking_fee, total_cost)
                    #booking.update_ticket_quantity()
                    Records.get_booking_list().append(booking)
            except Exception as e:
                print("Cannot load the booking file, running as if there is no previous booking file")

    
    #This method is used to calculate the price of each group ticket by getting the individual tickets in the group ticket,
    #computing their price and adding them. Also the 20% discount is also applied here.
    @staticmethod
    def get_group_ticket_price(group_ticket_list,group_ticket_quantity_list):
        totalamount = 0
        for i in range(0,len(group_ticket_list)):
            ticket = Operations.find_ticket(group_ticket_list[i])
            totalamount = totalamount + group_ticket_quantity_list[i]*float(ticket.price)
        totalamount = round(0.8 * totalamount,2)
        return totalamount

    #This method is used to return a customer object with the given search value(Customer ID/ Customer Name) 
    #If such a customer does not exist, a None is returned 
    @staticmethod
    def find_customer(search_value):
        for customer in Records.get_customer_list():
            if customer.ID == search_value or customer.name == search_value:
                return customer
        return None
    
    #This method is used to return a movie object with the given search value(movie ID/ movie Name) 
    #If such a movie does not exist, a None is returned 
    @staticmethod
    def find_movie(search_value):
        for movie in Records.get_movie_list():
            if movie.ID == search_value or movie.name == search_value:
                return movie
        return None
    
    #This method is used to return a ticket object with the given search value(ticket ID/ ticket Name) 
    #If such a ticket does not exist, a None is returned. This loops through two lists to search for a match
    #One that contains the basic tickets and another that contains the group tickets 
    @staticmethod
    def find_ticket(search_value):
        for ticket in Records.get_ticket_list():
            if ticket.ID == search_value or ticket.name == search_value:
                return ticket
        for ticket in Records.get_group_ticket_list():
            if ticket.ID == search_value or ticket.name == search_value:
                return ticket
        return None
    
    #This method is used to display all the given customer records. If there are no customers to display at the start,
    # a message will be displayed stating no current customers present
    @staticmethod
    def display_customer():
        if not Records.get_customer_list():
            print("There are no current customers present...")
        print("The customer details are as follows:")
        print("------------------------------------------\n")
        for customer in Records.get_customer_list():
            customer.display_info()
            print("\n------------------------------------------\n")
    
    #This method is used to display all the given movie records. If there are no movies to display at the start,
    # a message will be displayed stating no current movies present
    @staticmethod
    def display_movies():
        if not Records.get_movie_list():
            print("There are no current movies present...")
        print("Displaying the list of movies and their available seats:\n")
        print("Movie ID              Movie Name         Available Seats")
        for movie in Records.get_movie_list():
            movie.display_info()

    #This method is used to display all the given tickets. If there are no tickets to display at the start,
    # a message will be displayed stating no tickets present    
    @staticmethod
    def display_tickets():
        if not Records.get_ticket_list():
            print("There are no current tickets present...")
        print("Displaying the list of tickets types")
        print("Ticket ID            Ticket Name              Price")
        for ticket in Records.get_ticket_list():
            ticket.display_info()
        for ticket in Records.get_group_ticket_list():
            ticket.display_info()

    #This method is used to display all the given bookings. If there are no bookings to display at the start,
    # a message will be displayed stating no bookings present      
    @staticmethod
    def display_bookings():
        if not Records.get_booking_list():
            print("There are no current bookings present...")
        print("Displaying the list of all bookings")
        print("------------------------------------------------------------------------")  
        for booking in Records.get_booking_list():
            print("Customer ID: " + booking.customer.ID +"   Customer Name: "+ booking.customer.name)
            print("-----------------------------------")
            print("Movie ID: " + booking.movie.ID +"   Movie Name: "+ booking.movie.name)
            print("-----------------------------------")
            print("Ticket ID             Ticket Name         Quantity")
            for i in range(len(booking.ticket_list)):
                print(booking.ticket_list[i].ID.ljust(23," ")+booking.ticket_list[i].name.ljust(23," ")+ str(booking.quantity_list[i]))
            print("-----------------------------------")
            print("Total Cost :" + str(booking.total_ticket_cost)+" |  Booking fee: "+str(booking.booking_fee)+" |  Discount: "+str(booking.discount))
            print("------------------------------------------------------------------------")            

    #A method created to reduce code repetition. Used while displaying the receipt
    @staticmethod
    def printReceipt(key,value,paddingMax):
       paddingVar = paddingMax - len(key) 
       print((key+ value.rjust(paddingVar," ")))
    
    #This method lets the user add more movies in the form of comma seperated values
    @staticmethod
    def addMovies():
        newMovies = [x.strip() for x in input("Please enter the list of new movies\n").split(',')] 
        for x in newMovies:
            if str(x) == "":
                continue
            #Check if the movie already exisits
            if Operations.find_movie(x) :
                print("The movie named "+ x +" is already present. No action performed") 
            else:
                print("Adding movie : " + x)
                movie = Records.get_movie_list()[-1] 
                previousId = movie.ID
                newId = int(previousId[1:]) + 1
                newId = "M" + str(newId)
                newMovie = Movie(newId,x,50)
                Records.get_movie_list().append(newMovie)
    
    #Before displaying the current revenue generated, This method is called to update the movie's reveneues 
    # based on the bookings.
    @staticmethod
    def loadMovieRevenue():
        for booking in Records.get_booking_list():
            revenue_for_booking = float(booking.total_ticket_cost) + float(booking.booking_fee) - float(booking.discount)
            booking.movie.revenue += revenue_for_booking

    #This itterates through all the movie's revenues to display the most popular one.
    @staticmethod
    def displayMaxRevenue():
        max = 0
        for movie in Records.get_movie_list():
            if movie.revenue >= max :
                max = movie.revenue
                maxMovie = movie
        print("The movie with max revenue is diplayed below")
        print("Movie ID             Movie Name              Revenue")
        print(maxMovie.ID.ljust(23," ")+maxMovie.name.ljust(23," ")+ str(round(maxMovie.revenue,2)))

    #This method is used to reset the revenue of each movie to 0 after claculating revenues to avoid incorrect values being 
    #displayed or used for computation during the further processing of the program.
    @staticmethod
    def clearRevenue():
        for movie in Records.get_movie_list():
            movie.revenue = 0

    # This method creates a tabluar display of all movies along the rows and all the ticket types along the columns. 
    # The number of tickets are displayed for each movie along with the total revenue generated for that movie.
    # All the details are present in the booking object. The record of each movie, each ticket purchased and the total cost
    # To make it easier for accessing each data, All the relevant data is loaded in to dictionaries. 
    # An inital dictionary is dynamically created that holds a key value pair of each type of ticket and the number of seats
    # is set to 0. A copy of this dictionary is then assigned as value to another dictionary containing the movie names as keys.
    # Each booking obejct is itterated. From the booking object, the movie and the tickets are fetched and the 
    # relevant dictionaries are updated. String formatting and f strings are used to diplay the recorded data. 
    @staticmethod
    def displayAllMovieRecords():
        ticketCounts = {}
        movieDictionary = {}

        for ticket in Records.get_ticket_list():
            ticketCounts[ticket.name] = 0
        for ticket in Records.get_group_ticket_list():
            ticketCounts[ticket.name] = 0
        ticketCounts["Revenue"] = 0
            
        for movie in Records.get_movie_list():
            movieDictionary[movie.name] = ticketCounts.copy()
        for booking in Records.get_booking_list():
            for i in range(len(booking.quantity_list)):
                movieDictionary[booking.movie.name][booking.ticket_list[i].name] += booking.quantity_list[i]
            movieDictionary[booking.movie.name]["Revenue"] = round(float(booking.movie.revenue),2)
        
        max_column_width = max(len(column) for column in ticketCounts.keys())
        max_row_width = max(len(column) for column in movieDictionary.keys())
        header = " " * max_row_width + "  " + "  ".join(f"{column:^{max_column_width}}" for column in ticketCounts.keys())
        print(header)
        print("-" * len(header))
        for movieName in movieDictionary.keys():
            row_values = "  ".join(f"{value:^{max_column_width}}" for value in movieDictionary[movieName].values())
            print(movieName.ljust(max_row_width) + "  " + row_values)
        #The dictionaries are cleared after their intended purpose is served.
        del movieDictionary
        del ticketCounts

    #This method writes the customer details to the specified filename
    @staticmethod
    def write_customer(filename):
        with open(filename, "w") as file:
            for customer in Records.get_customer_list():
                if isinstance(customer, RewardFlatCustomer):
                    customer_id = customer.ID
                    name = customer.name
                    discount = str(RewardFlatCustomer.get_discount_rate())
                    line = customer_id+", "+name+", "+discount
                    file.write(line+ '\n')
                elif isinstance(customer, RewardStepCustomer):
                    customer_id = customer.ID
                    name = customer.name
                    discount = str(customer.discount_rate)
                    threshold =str(customer.get_threshold())
                    line = customer_id+", "+name+", "+discount+", "+threshold
                    file.write(line+ '\n')
                else :
                    customer_id = customer.ID
                    name = customer.name
                    line = customer_id+", "+name
                    file.write(line+ '\n')
    
    #This method writes the movie details to the specified filename
    @staticmethod
    def write_movie(filename):
        with open(filename, "w") as file:
            for movie in Records.get_movie_list():
                id = movie.ID
                name = movie.name
                seats = str(int(movie.seat_available))
                line = id+", "+name+", "+seats 
                file.write(line+ '\n')

    #This method writes the booking details to the specified filename
    @staticmethod
    def write_booking(filename):
        with open(filename, "w") as file:
            for booking in Records().get_booking_list():
                customer_id = booking.customer.ID
                movie_id = booking.movie.ID
                line = customer_id+", "+movie_id
                for i in range(len(booking.quantity_list)):
                    line = line +", "+booking.ticket_list[i].name + ", " + str(booking.quantity_list[i])
                discount = str(booking.discount)
                cost = str(booking.total_ticket_cost)
                bookingfee = str(booking.booking_fee)
                line = line+", "+discount+", "+bookingfee+", "+cost
                file.write(line+ '\n')

#------------------------------------------------------------------------------------------

Operations()
