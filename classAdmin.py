import os
import csv
from models import User, Product
from utils import read_from_csv, write_to_csv
from config import generate_short_uuid

class Admin(User):
    def __init__(self, userId, username, password, isAdmin):
        super().__init__(userId, username, password, isAdmin)

    def add_new_product(self):
        productId = generate_short_uuid()
        name = input("Name of product: ")
        price = input("Price of product: ")
        stock = input("Stock of product: ")
        new_product = Product(productId, name, price, stock)
        product_dict = new_product.to_dict()
        print(product_dict)
        write_to_csv("products", product_dict, "a")



    def edit_product(self):
        products = self.list_all_products()
        product_id = input("Product id to edit: ")
        new_name = input("Name: ")
        new_price = input("Price: ")
        new_stock = input("Stock: ")
        updated_product = Product(product_id, new_name, new_price, new_stock)
        updated_product_dict = updated_product.to_dict()
        found = False
        new_product_list = []
        for product in products:
            if(product['productId'] == product_id):
                found = True
                new_product_list.append(updated_product_dict)
            else:
                new_product_list.append(product)
    
        if(found == False):
            print("productId not found within products.csv file")
            return 
        print(new_product_list)
        write_to_csv("products", new_product_list, "w")


    def delete_product(self):
        products = self.list_all_products()
        product_id = input("Product id to delete: ")
        found = False
        new_product_list = []
        for product in products:
            if(product['productId'] == product_id):
                found = True
            else:
                new_product_list.append(product)
    
        if(found == False):
            print("productId not found within products.csv file")
            return 
        write_to_csv("products", new_product_list, "w")

    def view_orders():
        print("view orders")

    def view_orders_range():
        print("view orders range")