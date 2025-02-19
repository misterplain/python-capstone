import uuid
import csv
import os
from utils import generate_short_uuid, Product

def list_all_products():
    """Read user data from CSV and return a list of dictionaries."""
    products = []
    try:
        with open("products.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
    except FileNotFoundError:
        print(f"Warning: 'products.csv' not found. Creating a new one.")
    for product in products:
        print(f'{product["productId"]} - ${product["price"]} - stock: {product["stock"]} - name: {product["name"]}')
    return products

def add_new_product():
    print("new product")
    productId = generate_short_uuid()
    name = input("Name of product: ")
    price = input("Price of product: ")
    stock = input("Stock of product: ")
    new_product = Product(productId, name, price, stock)
    product_dict = new_product.to_dict()
    print(product_dict)
    fieldnames = ["productId", "name", "price", "stock"]
    file_exists = os.path.exists("products.csv")
    try:
        with open("products.csv", "a", newline="") as file: 
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(product_dict) 
    except IOError as e:
        print(f"Error: Unable to write to products.csv")


def edit_product():
    products = list_all_products()
    print(products)
    product_id = input("Product id to edit: ")
    new_name = input("Name: ")
    new_price = input("Price: ")
    new_stock = input("Stock: ")
    updated_product = Product(product_id, new_name, new_price, new_stock)
    updated_product_dict = updated_product.to_dict()

    ##check if productID is in list
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
    fieldnames = ["productId", "name", "price", "stock"]
    try:
        with open("products.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(new_product_list)
    except IOError:
        print(f"Error: Unable to write to 'products.csv.")





def delete_product():
    print("delete product")

def view_orders():
    print("view orders")

def view_orders_range():
    print("view orders range")