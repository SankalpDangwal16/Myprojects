# -*- coding: utf-8 -*-
"""
Created on Sat May 20 18:51:49 2023

@author: sanka
"""
class Customer:
    def __init__(self, customer_id, customer_name, discount_value, threshold):
        self.customer_id = customer_id
        self.customer_name = customer_name 
        #self.discount_value = discount_value
       # self.threshold = threshold
     
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
        
        def read_customers(self, file_name):
            with open(file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = lines.strip()
                    customer_data = line.split(',')
                    customer_id = customer_data[0].strip()
                    customer_name = customer_data[1].strip()
                    if customer_id.startswith('F'):
                        discount_value = float(customer_data[2]).strip()
                        customer = Customer(customer_id, customer_name, discount_value)
                    elif customer.startswith('S'):
                        discount_value = float(customer_data[2]).strip()
                        threshold = int(customer_data[3]).strip()
                        customer = Customer(customer_id, customer_name, discount_value, threshold)
                    else:
                        customer = Customer(customer_id, customer_name)
                    self.customer_list.append(customer)
             