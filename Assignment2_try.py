class Customer:
    def __init__(self, id, name, reward_program):
        self.id = id
        self.name = name
        self.reward_program = reward_program

    def __str__(self):
        return f"Customer ID: {self.id}, Name: {self.name}, Reward Program: {self.reward_program}"


class CustomerManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self, identifier):
        for customer in self.customers:
            if customer.id == identifier or customer.name == identifier:
                return customer
        return None

    def adjust_reward_flat_discount(self, discount_rate):
        if not isinstance(discount_rate, (int, float)) or discount_rate <= 0:
            raise ValueError("Invalid discount rate. Please enter a positive number.")
        for customer in self.customers:
            if isinstance(customer.reward_program, RewardFlat):
                customer.reward_program.adjust_discount_rate(discount_rate)

    def adjust_reward_step_discount(self, customer_identifier, discount_rate):
        if not isinstance(discount_rate, (int, float)) or discount_rate <= 0:
            raise ValueError("Invalid discount rate. Please enter a positive number.")
        customer = self.get_customer(customer_identifier)
        if customer and isinstance(customer.reward_program, RewardStep):
            customer.reward_program.adjust_discount_rate(discount_rate)
        else:
            raise ValueError("Invalid customer. Please enter a valid RewardStep customer.")


class RewardProgram:
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate

    def adjust_discount_rate(self, new_discount_rate):
        self.discount_rate = new_discount_rate


class RewardFlat(RewardProgram):
    def __init__(self, discount_rate):
        super().__init__(discount_rate)


class RewardStep(RewardProgram):
    def __init__(self, discount_rate):
        super().__init__(discount_rate)


class Movie:
    def __init__(self, id, title, price):
        self.id = id
        self.title = title
        self.price = price

    def __str__(self):
        return f"Movie ID: {self.id}, Title: {self.title}, Price: {self.price}"


class MovieManager:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, identifier):
        for movie in self.movies:
            if movie.id == identifier or movie.title == identifier:
                return movie
        return None

    def display_most_popular_movie(self):
        if not self.movies:
            return "No movies available."
        max_revenue = max(movie.total_revenue for movie in self.movies)
        popular_movies = [movie for movie in self.movies if movie.total_revenue == max_revenue]
        result = "Most Popular Movie(s):\n"
        for movie in popular_movies:
            result += f"{str(movie)}\n"
        return result


class TicketType:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Ticket Type ID: {self.id}, Name: {self.name}, Price: {self.price}"


class TicketManager:
    def __init__(self):
        self.ticket_types = []

    def add_ticket_type(self, ticket_type):
        self.ticket_types.append(ticket_type)

    def get_ticket_type(self, identifier):
        for ticket_type in self.ticket_types:
            if ticket_type.id == identifier or ticket_type.name == identifier:
                return ticket_type
        return None


class Booking:
    def __init__(self, customer, movie, tickets, discount, booking_fee):
        self.customer = customer
        self.movie = movie
        self.tickets = tickets
        self.discount = discount
        self.booking_fee = booking_fee
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        ticket_cost = sum(ticket.quantity * ticket.ticket_type.price for ticket in self.tickets)
        discount_amount = ticket_cost * self.discount
        return ticket_cost - discount_amount + self.booking_fee


class BookingManager:
    def __init__(self):
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def display_all_bookings(self):
        if not self.bookings:
            return "No bookings available."
        result = "All Bookings:\n"
        for booking in self.bookings:
            result += f"Customer: {booking.customer.name}, Movie: {booking.movie.title}, " \
                      f"Tickets: {', '.join(str(ticket) for ticket in booking.tickets)}, " \
                      f"Discount: {booking.discount}, Booking Fee: {booking.booking_fee}, " \
                      f"Total Cost: {booking.total_cost}\n"
        return result


class Operations:
    def __init__(self, customer_manager, movie_manager, ticket_manager, booking_manager):
        self.customer_manager = customer_manager
        self.movie_manager = movie_manager
        self.ticket_manager = ticket_manager
        self.booking_manager = booking_manager

    def purchase_ticket(self):
        customer_id = input("Enter customer ID: ")
        movie_id = input("Enter movie ID: ")

        customer = self.customer_manager.get_customer(customer_id)
        movie = self.movie_manager.get_movie(movie_id)

        if customer and movie:
            ticket_types = []
            ticket_quantities = []
            while True:
                ticket_type_id = input("Enter ticket type ID (0 to finish): ")
                if ticket_type_id == '0':
                    break
                ticket_type = self.ticket_manager.get_ticket_type(ticket_type_id)
                if ticket_type:
                    ticket_types.append(ticket_type)
                    quantity = int(input("Enter ticket quantity: "))
                    ticket_quantities.append(quantity)
                else:
                    print("Invalid ticket type ID. Please enter a valid ID.")
            if ticket_types and ticket_quantities:
                tickets = [Ticket(ticket_type, quantity) for ticket_type, quantity in
                           zip(ticket_types, ticket_quantities)]
                discount = customer.reward_program.discount_rate
                booking_fee = 5  # Example value, you can change it
                booking = Booking(customer, movie, tickets, discount, booking_fee)
                self.booking_manager.add_booking(booking)
                print("Ticket(s) purchased successfully.")
            else:
                print("No tickets selected.")
        else:
            print("Invalid customer ID or movie ID. Please enter valid IDs.")

    def add_movie(self):
        movie_id = input("Enter movie ID: ")
        movie_title = input("Enter movie title: ")
        movie_price = float(input("Enter movie price: "))
        movie = Movie(movie_id, movie_title, movie_price)
        self.movie_manager.add_movie(movie)
        print("Movie added successfully.")

    def adjust_reward_flat_discount(self):
        discount_rate = float(input("Enter the new discount rate for RewardFlat customers: "))
        self.customer_manager.adjust_reward_flat_discount(discount_rate)
        print("RewardFlat discount rate adjusted successfully.")

    def adjust_reward_step_discount(self):
        customer_identifier = input("Enter customer ID or name: ")
        discount_rate = float(input("Enter the new discount rate for the customer: "))
        try:
            self.customer_manager.adjust_reward_step_discount(customer_identifier, discount_rate)
            print("RewardStep discount rate adjusted successfully.")
        except ValueError as e:
            print(str(e))

    def display_all_bookings(self):
        bookings = self.booking_manager.display_all_bookings()
        print(bookings)

    def display_most_popular_movie(self):
        popular_movies = self.movie_manager.display_most_popular_movie()
        print(popular_movies)


# Example usage:
if __name__ == "__main__":
    # Creating instances of the managers
    customer_manager = CustomerManager()
    movie_manager = MovieManager()
    ticket_manager = TicketManager()
    booking_manager = BookingManager()

    # Creating instances of the customers, movies, and ticket types
    customer1 = Customer("1", "John Doe", RewardFlat(0.1))
    customer2 = Customer("2", "Jane Smith", RewardStep(0.2))

    movie1 = Movie("1", "Movie 1", 10)
    movie2 = Movie("2", "Movie 2", 15)

    ticket_type1 = TicketType("1", "Adult", 10)
    ticket_type2 = TicketType("2", "Child", 5)

    # Adding customers, movies, and ticket types to their respective managers
    customer_manager.add_customer(customer1)
    customer_manager.add_customer(customer2)

    movie_manager.add_movie(movie1)
    movie_manager.add_movie(movie2)

    ticket_manager.add_ticket_type(ticket_type1)
    ticket_manager.add_ticket_type(ticket_type2)

    # Creating an instance of Operations and passing the managers to it
    operations = Operations(customer_manager, movie_manager, ticket_manager, booking_manager)

    # Example usage of the operations
    operations.purchase_ticket()
    operations.add_movie()
    operations.adjust_reward_flat_discount()
    operations.adjust_reward_step_discount()
    operations.display_all_bookings()
    operations.display_most_popular_movie()