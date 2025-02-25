from utils import read_from_csv, write_to_csv

class User:
    def __init__(self, userId, username, password, isAdmin, orders=None, cart=None):
        self.userId = userId
        self.username = username
        self.password = password
        self.isAdmin = isAdmin
    def to_dict(self):
        """Convert User object to dictionary for CSV writing."""
        return {
            "userId": self.userId,
            "username": self.username,
            "password": self.password,
            "isAdmin": self.isAdmin
        }

    def list_all_products(self):
        all_products = read_from_csv("products")
        return all_products
    def list_all_cart_items(self):
        all_cart_items = read_from_csv("products-cart")
        return all_cart_items
    def list_user_cart(self):
        all_cart_items = read_from_csv("products-cart")
        user_cart_items = []
        for product in all_cart_items:
            if(product["userId"] == self.userId):
                user_cart_items.append(product)
        return user_cart_items
    
    def list_all_orders(self):
        all_orders = read_from_csv("orders")
        return all_orders
    
    def get_individual_order(self):
        all_orders = read_from_csv("orders")
        order_id = input("Please enter order ID: ")
        for order in all_orders:
            if(order["orderId"] == order_id):
                return order
        return None
    
    def list_user_orders(self):
        all_orders = read_from_csv("orders")
        user_orders = []
        for order in all_orders:
            if(order["userId"] == self.userId):
                user_orders.append(order)
        return user_orders
    
    def list_order_items(self, individual_order):
        all_order_items = read_from_csv("order-items")
        user_order_items = []
        for order in all_order_items:
            if(order["orderId"] == individual_order["orderId"]):
                user_order_items.append(order)
        return user_order_items

class Product:
    def __init__(self, productId, name, price, stock):
        self.productId = productId
        self.name = name
        self.price = price
        self.stock = stock 
    def to_dict(self):
        """Convert User object to dictionary for CSV writing."""
        return {
            "productId": self.productId,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }
    
class ProductCart:
    def __init__(self, productId, userId,name, quantity, price):
        self.productId = productId
        self.userId = userId
        self.name = name
        self.quantity = quantity
        self.price = price
    def to_dict(self):
        """Convert User object to dictionary for CSV writing."""
        return {
            "productId": self.productId,
            "userId": self.userId,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }
    
class Order:
    def __init__(self,orderId, userId, datePlaced, totalPrice):
        self.orderId = orderId
        self.userId = userId
        self.datePlaced = datePlaced
        self.totalPrice = totalPrice
    def to_dict(self):
        """Convert User object to dictionary for CSV writing."""
        return {
            "orderId": self.orderId,
            "userId": self.userId,
            "datePlaced": self.datePlaced,
            "totalPrice": self.totalPrice
        }
    
class OrderItem:
    def __init__(self,orderId, userId, productId, name, quantity, price):
        if isinstance(productId, tuple):
            print(f"Tuple Detected in OrderItem: {productId}")
            productId = productId[0]  # Extract the first element
        self.orderId = orderId
        self.userId = userId
        self.productId = productId
        self.name = name
        self.quantity = quantity
        self.price = price

    def to_dict(self):
        """Convert User object to dictionary for CSV writing."""
        return {
            "orderId": self.orderId,
            "userId": self.userId,
            "productId": self.productId,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }