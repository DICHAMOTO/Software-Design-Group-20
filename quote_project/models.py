from datetime import datetime
from quote_project import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    address1 = db.Column(db.String(100), unique=False, nullable=False)
    address2 = db.Column(db.String(100), unique=False, nullable=True)
    city = db.Column(db.String(100), unique=False, nullable=False)
    state = db.Column(db.String(20), unique=False, nullable=False)
    zip = db.Column(db.String(10), unique=False, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    quotes = db.relationship('Quote', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.address1}', '{self.address2}', {self.city}', '{self.state}', " \
               "'{self.zip}') "


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    delivery_date = db.Column(db.String(10), unique=False, nullable=False)
    request_gallons = db.Column(db.Float, nullable=False)
    suggested_price = db.Column(db.Float)
    date_quoted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Quote('{self.delivery_date}', '{self.request_gallons}', '{self.suggested_price}', '{self.total}', '{self.date_quoted}')"