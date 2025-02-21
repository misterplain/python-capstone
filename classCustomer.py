import os
import csv
import datetime
from models import User, Product, ProductCart, Order, OrderItem
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
        # print(all_products)

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
            # print(new_cart_item_dict)

            write_to_csv(endpoint, new_cart_item_dict, method)
            break  

    def remove_item_from_cart(self, endpoint, method):
        products_in_carts = self.list_cart_items(self)
        # print(products_in_carts)
        product_id = input("Product id to remove:")
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

        print(found)
        print(new_cart)

        write_to_csv(endpoint, new_cart,method)

    def place_order(self):
        
        # get all cart items
        products_in_carts = self.list_cart_items(self)
        # print(products_in_carts)
        products_in_usercart = []
        products_remaining = []
        for product in products_in_carts:
            if product["userId"] == self.userId:
                products_in_usercart.append(product)
            else:
                products_remaining.append(product)
        print("products remaining: ")
        print(products_remaining)
        print("products in user cart: ")
        print(products_in_usercart)

        order_id = generate_short_uuid()
        total_price = 0
        for product in products_in_usercart:
            total_price += int(product["price"]) * int(product["quantity"])
        print("total price of user cart: ")
        print(total_price)

        ##place new order
        order_date = datetime.datetime.now().strftime("%c")
        new_order = Order(order_id, self.userId, order_date, total_price)
        new_order_dict = new_order.to_dict()
        print("new order: ")
        print(new_order_dict)

        ##add order items to order-items
        ##get all products, for each product ordered, filter through all products and if product Id matches, remove the stock amount from that product and add it to updated_products array, if the productId does not match, add the product to updated_products array
        all_products = self.list_all_products()
        print("all products:")
        print(all_products)
        products_ordered = []
        updated_products = []
        for product in products_in_usercart:
            product_ordered = OrderItem(order_id, self.userId, product["productId"], product["name"], product["quantity"], product["price"])
            product_ordered_dict = product_ordered.to_dict()
            # print(product["productId"])
            products_ordered.append(product_ordered_dict)
            for item in all_products:
                if item["productId"] == product["productId"]:
                    item["stock"] = int(item["stock"]) - int(product["quantity"])

        # for product in products_ordered:
        #     for item in all_products:
        #         if item["productId"] == product["productId"]:
        #             item["stock"] = int(item["stock"]) - int(product["quantity"])
        #             updated_products.append(item)

        #         else: 
        #             updated_products.append(item)
        print("products ordered: ")
        print(products_ordered)
        print("all products after updating:")
        print(all_products)

        # print("updated products: ")
        # print(updated_products)


        ##get all products, get products ordered


        ####basically, write to products cart the remaining variable and write to order-items the products_in_usercart

        # get all products

        #new cart - remove all items associated with this user
        #new order - order number, time, price
        #new order items - order id, user id, quaniy price, name 
        #new products - 

        ## for each cart item, find it's product and if the stock is higher in the cart, go back and tell customer they need to remove item from cart, check the listing, and add a different emount of that item to cart

        #if there is stock available for each item

            

            
            



            # for product in products_in_carts:
                # if product("productId")  == product_to_remove and product("userId") == self.userId:
                #     found_product=True
                # else:
                #     new_cart.append(product)


