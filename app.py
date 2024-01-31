from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Car

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db.init_app(app)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/payment')
def payment():
    return render_template("payment.html")


@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


if __name__ == "__main__":
    app.run(debug=True)
