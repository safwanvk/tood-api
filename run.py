from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
BASEDIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(100), unique=True)

    def __int__(self, todo):
        self.todo = todo


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'todo')


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
