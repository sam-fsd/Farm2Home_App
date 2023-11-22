#!/usr/bin/python3
"""creates a Flask app instance"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@localhost:3306/foodbank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello World!"


if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True, host='127.0.0.1', port=5000)
