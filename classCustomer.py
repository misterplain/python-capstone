import os
import csv
from models import User, Product, ProductCart
from utils import read_from_csv, write_to_csv
from config import generate_short_uuid

class Customer(User):
    def __init__(self, userId, username, password, isAdmin):
        super().__init__(userId, username, password, isAdmin)

    def printCreation(self):
        print("customer created")

    def list_all_products(self):
        products = read_from_csv("products")
        for product in products:
            print(f'{product["productId"]} - ${product["price"]} - stock: {product["stock"]} - name: {product["name"]}')
        return products
    
    def list_cart_items(self, endpoint):
        products = read_from_csv("products-cart")
        for product in products:
            print(f'{product["userId"]} - {product["productId"]} - {product["name"]} - {product["quantity"]} - {product["price"]}')
        return products
    
    def add_item_to_cart(self, endpoint, method):
        products_in_carts = self.list_cart_items(self)

        # dictionary for all products
        all_products = {product["productId"]: product for product in read_from_csv("products")}
        print(all_products)

        while True:
            product_id = input("Product ID to add to cart: ")
            quantity = input("Quantity: ")

            if not quantity.isdigit():
                print("Please enter a valid quantity.")
                continue
            quantity = int(quantity)

            # iterate through products_in_carts to check if item already in cart
            if any(product["productId"] == product_id and product["userId"] == self.userId for product in products_in_carts):
                print("Item already in cart. Choose a different item.")
                continue

            # if product even exists
            if product_id not in all_products:
                print("Product not found. Try again.")
                continue
            
            found_product = all_products[product_id]

            # check stock availability
            if int(found_product["stock"]) < quantity:
                print(f"Not enough stock available. Current stock: {found_product['stock']}")
                continue

            # add item to cart
            new_cart_item = ProductCart(product_id, self.userId, found_product["name"], quantity, found_product["price"])
            new_cart_item_dict = new_cart_item.to_dict()
            print(new_cart_item_dict)

            write_to_csv(endpoint, new_cart_item_dict, method)
            break  

