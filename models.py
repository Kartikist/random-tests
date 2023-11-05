from . import db  # Import the SQLAlchemy instance from your package

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    useremail = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)
