import os
import csv
import datetime
from models import User, Product, ProductCart, Order, OrderItem
from utils import read_from_csv, write_to_csv
from config import generate_short_uuid

class Customer(User):
    def __init__(self, userId, username, password, isAdmin):
        super().__init__(userId, username, password, isAdmin)
    
    def add_item_to_cart(self):
        products_in_carts = self.list_all_cart_items()
        all_products = {product["productId"]: product for product in read_from_csv("products")}

        while True:
            product_id = input("Product ID to add to cart: ")
            quantity = input("Quantity: ")

            if not quantity.isdigit():
                print("Please enter a valid quantity.")
                continue
            quantity = int(quantity)

            if any(product["productId"] == product_id and product["userId"] == self.userId for product in products_in_carts):
                print("Item already in cart. Choose a different item.")
                continue

            if product_id not in all_products:
                print("Product not found. Try again.")
                continue
            
            found_product = all_products[product_id]

            if int(found_product["stock"]) < quantity:
                print(f"Not enough stock available. Current stock: {found_product['stock']}")
                continue

            new_cart_item = ProductCart(product_id, self.userId, found_product["name"], quantity, found_product["price"])
            new_cart_item_dict = new_cart_item.to_dict()

            write_to_csv("products-cart", new_cart_item_dict, "a")
            break

    def remove_item_from_cart(self):
        products_in_carts = self.list_all_cart_items()
        product_id = input("Product id to remove: ")
        found = []
        new_cart = []

        for product in products_in_carts:
            if(product["productId"] == product_id):
                if(product["userId"] == self.userId):
                    found.append(product)
                else:
                    new_cart.append(product)
            else:
                new_cart.append(product)

        write_to_csv("products-cart", new_cart,"w")

    def place_order(self):
        
        # Get cart items, filter out items that are in user cart, re-write products-cart file with remaining items
        products_in_carts = self.list_all_cart_items()
        products_in_usercart = []
        products_remaining = []
        for product in products_in_carts:
            if product["userId"] == self.userId:
                products_in_usercart.append(product)
            else:
                products_remaining.append(product)
        write_to_csv("products-cart", products_remaining, "w")

        # Generate order id and calculate total price
        order_id = generate_short_uuid()
        total_price = 0
        for product in products_in_usercart:
            total_price += int(product["price"]) * int(product["quantity"])

        ##Place new order and append to orders-csv
        order_date = datetime.datetime.now().strftime("%c")
        new_order = Order(order_id, self.userId, order_date, total_price)
        new_order_dict = new_order.to_dict()
        write_to_csv("orders", new_order_dict, "a")

        all_products = self.list_all_products()
        products_ordered = []
        for product in products_in_usercart:
            product_ordered = OrderItem(order_id, self.userId, product["productId"], product["name"], product["quantity"], product["price"])
            product_ordered_dict = product_ordered.to_dict()
            write_to_csv("order-items", product_ordered_dict, "a")
            products_ordered.append(product_ordered_dict)
            for item in all_products:
                if item["productId"] == product["productId"]:
                    item["stock"] = int(item["stock"]) - int(product["quantity"])
                    break
        write_to_csv("products", all_products, "w")
        print("Order placed successfully.\n")


            


