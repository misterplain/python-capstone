import uuid
import csv
import json

def generate_short_uuid():
    return str(uuid.uuid4())[:8]

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
    
##subclass for product_in_cart
    
class Order:
        def __init__(self, orderId, userId, datePlaced, items):
             self.orderId = orderId
             self.userId = userId
             self.datePlaced = datePlaced
             self.items = items
        def to_dict(self):
            """Convert User object to dictionary for CSV writing."""
            return {
                "orderId": self.orderId,
                "userId": self.userId,
                "datePlaced": self.datePlaced,
                "items": self.items
            }
        

##subclass for order_item