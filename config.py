import uuid 

def generate_short_uuid():
    return str(uuid.uuid4())[:8]

endpoint_dict = {
    "users": ['data-users.csv', ["userId", "username", "password", "isAdmin"]],
    "products": ['data-products.csv', ["productId", "name", "price", "stock"]],
    "products-cart": ['data-products-cart.csv', ["productId", "userId","name", "quantity", "price"]],
    "orders": ['data-orders.csv', ["orderId", "userId", "datePlaced", "totalPrice"]],
    "order-items": ['data-order-items.csv', ["orderId", "userId", "productId", "name","quantity", "price"]],
}