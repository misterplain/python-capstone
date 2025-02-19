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