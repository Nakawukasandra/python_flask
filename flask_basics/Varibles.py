
from flask import Flask
app = Flask(__name__)#creating the app varible


@app.route('/home')
def home():
    return '<h2>NAKAWUKA SANDRA</h2>'







