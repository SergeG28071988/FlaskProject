from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Car {self.id}"
    

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/create-car', methods=['POST', 'GET'])
def create_car():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        year = request.form['year']
        color = request.form['color']

        car = Car(brand=brand, model=model, year=year, color=color)
        try:
            db.session.add(car)
            db.session.commit()
            return redirect('/cars')
        except:
            return "При добавлении автомобиля произошла ошибка!!!"
    else:
        return render_template("create-car.html")
    

@app.route('/cars')
def cars():
    cars = Car.query.order_by(Car.year).all()
    return render_template("cars.html", cars=cars)


@app.route('/cars/<int:id>')
def car_detail(id):
    car = Car.query.get(id)
    return render_template("car-detail.html", car=car)



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
    with app.app_context():
        db.create_all()
    app.run(debug=True)
