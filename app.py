from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'orders.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(100))
    item = db.Column(db.String(100))
    quantity = db.Column(db.Integer)

# Create DB if not exist
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    customer = request.form["customer"]
    item = request.form["item"]
    quantity = request.form["quantity"]

    new_order = Order(customer=customer, item=item, quantity=quantity)
    db.session.add(new_order)
    db.session.commit()

    message = f"Order saved: {quantity} x {item} for {customer}"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
