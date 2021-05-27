from market import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=False)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(12), nullable=False, unique=False)
    description = db.Column(db.String(1024), nullable=False)

    def __repr__(self):
        return f"item {self.name}"