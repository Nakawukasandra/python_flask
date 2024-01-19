from flask import Flask


app = Flask(__name__)#creating the app instance


@app.route('/')
def home():
    return '<h2>Welcome to Flask Mastery</h2>'


if __name__  == '_main_':
    app.run(debug=True)




