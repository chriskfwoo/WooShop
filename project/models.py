from project import db


class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Float(128), nullable=False)
    inventory_count = db.Column(db.Integer, nullable=False)

    def __init__(self, title, price, inventory_count):
        self.title = title
        self.price = price
        self.inventory_count = inventory_count

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'inventory_count': self.inventory_count
        }

    def is_available(self):
        return self.inventory_count > 0

    def remove_inventory(self, value):
        self.inventory_count = self.inventory_count - value
