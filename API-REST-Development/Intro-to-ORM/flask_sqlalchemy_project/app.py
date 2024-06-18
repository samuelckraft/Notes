from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow import ValidationError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:654U7jsv@localhost/e_commerce_db'
                                                                #user:password@location/database

db = SQLAlchemy(app)
ma = Marshmallow(app)

class customerschema(ma.Schema):
    name = fields.String(required = True) #fields are like columns on a database; things we need or want to keep track of
    email = fields.String(required = True) #not required unless we do this required=true is there
    phone = fields.String(required = True)
    

    class Meta:
        fields = ('name', 'email', 'phone', 'id')

customer_schema = customerschema()
customers_schema = customerschema(many=True)
#models (create tables and columns)

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(320))
    phone = db.Column(db.String(15))
    orders = db.relationship('order', backref = 'customer') #Establishing relationship with orders table, doesn't appear as column


class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date, nullable = False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))


#one to one relationship (customers to customer accounts)
class CustomerAccount(db.Model):
    __tablename__ = 'Customer Accounts'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.relationship('Customer', backref = 'customer_account', uselist = False) #SQLalchemy usually treats these like lists, but uselist being false means it will treat it like a single item


#many to many relationship 
order_product = db.Table('Order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key = True),
    db.Column('product_id', db.Integer, db.ForeignKey('Products.id'), primary_key = True)
)

class product(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    price = db.Column(db.Float, nullable = False)
    orders = db.relationship('order', secondary = order_product, backref = db.backref('products'))


#initialize the database and create tables
with app.app_context():
    db.create_all() #checks database to see if tables already exist; if it does, then it won't attempt to recreate or modify its structure

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/customers', methods = ['GET'])
def get_customers():
    customers = Customer.query.all() #this is our sql select query
    return customers_schema.jsonify(customers)

@app.route('/customers', methods = ['POST'])
def add_customer():
    try:
        #validate and deserialize input
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    new_customer = Customer(name = customer_data['name'], email = customer_data['email'], phone = customer_data['phone'])
    db.session.add(new_customer)
    db.session.commit()

    return jsonify({'message': "New customer added successfully"}), 201


@app.route('/customers/<int:id>', methods = ['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer.name = customer_data['name']
    customer.email = customer_data['email']
    customer.phone = customer_data['phone']
    db.session.commit()

    return jsonify({'message': 'Customer details updated succesfully'}), 200

@app.route('/customers/<int:id>', methods = ['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()

    return jsonify({"message": 'Customer deleted successfully'}), 200

