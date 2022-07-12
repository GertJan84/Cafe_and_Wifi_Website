from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Cafes(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route('/')
def home():
    return render_template('index.html', all_caffes=[cafes for cafes in Cafes.query.all()])


@app.route('/add', methods=['POST'])
def add():
    if request.method == "POST":
        name = request.form.get('name')
        loc = request.form.get('loc')
        soc = request.form.get('soc').lower() == "true"
        toilet = request.form.get('toilet').lower() == "true"
        wifi = request.form.get('wifi').lower() == "true"
        calls = request.form.get('calls').lower() == "true"
        seats = request.form.get('seats')
        price = request.form.get('price')
        img_url = request.form.get('img_url')
        map_url = request.form.get('map_url')
        new_cafe = Cafes(name=name, map_url=map_url, img_url=img_url, location=loc, has_sockets=soc, has_toilet=toilet, has_wifi=wifi, can_take_calls=calls, seats=seats, coffee_price=price)
        db.session.add(new_cafe)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
