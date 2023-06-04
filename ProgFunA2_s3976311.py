import sys
# Student Name : Shubham Pai
# Student ID   : S3976311
# Highest part Attempted : HD (Completed)


# Analysis
#-------------
# The program follows an obejct oriented approach where each component of the program has been 
# spearated into objects with each object having its own attributes and methods.
# Access modifiers have been extensively used to prevent accidently modification of object details.
# Getters and setters for each object were implemented for easier access to object variables. Inheritance
# has been used whereever applicable to reduce the code size and make use of the object oriented functionality.
# The initial challenge while implementing this functionality in part 1 was the inability to test the code while 
# initializing the classes, variables and methods. It was after I finished writing 400 lines of code, that I could
# finally start testing my program. Few minor and some major bugs had to be fixed. As there were no error scenarios
# to be handled nor were there any incorrect input values, the first part(pass level) was straightforward and less 
# complicated while executing. But the initialization process consumed alot of time and efforts. The credit level
# had relatively smaller but trickier requirements where I was forced to use custom exceptions instead of while 
# loops to ensure proper input. I made use of recursion along with exception handling to get the desired result.
# The introduction of group tickets heavily increased the complexity of the program where 1 ticket now could occupy
# more than 1 seats and logic to handle such scenarios had to be implemented. Reading the group tickets from the
# text files was also a challenge as now I couldn't be sure about the number of values each line read would contain.
# The fact that we could always rely that there would not be any invalid input helped when implementing these requirements
# The DI level added the requirement to take multiple inputs. Luckily, object oriented programs follow the concept of modularity
# and the ability to make modifications to a part of the program and not risking the entire program crashing helped implement
# the given requirements. Modifications had to be made to the Booking object as all the ticket purchases would be part of 
# a singular booking. The methods to adjust the discount rates for the customers were implemented as part of the pass-level.
# Also the method to fetch the customer details was implemeted. So I had to just implement a method to correctly invoke those 
# methods. HD required me to read the booking details and preload the booking object. Reading the booking details was a challenge
# but implementing the logic to read the group ticket details had given me an idea as to how I can read an unknown amount of 
# comma seperated values. As a booking object would store all the details including the movie and the ticket details, It was straight 
# forward task to display all the booking details. Acception command line arguments requied some minor changes to the initiliaztion 
# process of the program to handle incorrect amount of arguments provided and other scenarios. Given the requirement for formatting 
# data and presenting them accurately was given in the first assignments, I refined my skills and was able to use string formatting 
# effectively to display all the movie records. The logic to upload all the records back to the files had reduced complexity because
# of the Records class which was storing all the details in the form of lists and made it simpler to complete the task.


#This class is used to store each individual basic customer details
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
#------------------------------------------------------------------------------------------

#This class is used to store each individual RewardFlat customer details[Child of Customer]
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

#------------------------------------------------------------------------------------------

#This class is used to store each individual RewardStep customer details[Child of Customer]
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

#This class is used to store each individual movie details
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

#This class is used to store each ticket details
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

#This class is used to store each group ticket details[Child of Ticket]
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

#This class stores all booking details. It records each booking as an object and links the customer, movie and ticket objects
# associated with the booking with the particular booking object
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

    #This method computes the cost of each booking. The booking object which is sent to this method had all the details needed to 
    #compute total cost. The customer details lets me know if a discount should be applied. The movie tells me which seats to be adjusted
    #The two lists store the ticket type and quantity of each ticket. Together combined, its sufficient to process the given data 
    #and compute the cost of this particular booking. This method returns the booking fee, total ticket cost and also the applicable 
    #dicount.
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
    
    #Everytime a booking is successful, this method is called to update the number of available seats
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

#------------------------------------------------------------------------------------------

#This class is the central repository of data, every existing customer, movie, ticket and booking performed is recorded in this class.
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

#This is used to create custom exceptions to display customized messages
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

#------------------------------------------------------------------------------------------

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
    
    #This method performs the basic operations of purchasing a ticket
    @staticmethod
    def purchase_ticket():

        customer_search_value = input("Please enter your ID / name\n").strip()
        customer = Operations.find_customer(customer_search_value)
        movie = Operations.input_movie()
        tickets = Operations.input_ticket()
        quantities = Operations.input_Quantity(movie, tickets)

         #This block of code is for registering a new customer.
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

        #We create the booking object here with the gathered details and the cost of the booking is calculated.
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

    #This method is used to update the discount rate of RewardFlat customer
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

    #The methods listed below with method name in the format 'input_value' are recursive methods. 
    #This means that if an incorrect value is entered, These methods will call themselves and ask the user to enter the correct details.

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

    #Method to get quantity details. Note that in this method, the input value is given in the form of comma sepearated values
    #Additionally, every input is cross verified with the movie to see if the required number of seats are available. 
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
