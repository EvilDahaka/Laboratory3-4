from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(73), nullable=False)
    description = db.Column(db.String(178), nullable=False)
    price = db.Column(db.Float, nullable=False) 
    image_url = db.Column(db.String(200), nullable=False)
    


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    items = [
        {"name": "Samsung Galaxy S23", "description": "Остання модель Galaxy з потужною камерою та швидким процесором.", "price": 10850, "image_url": "https://via.placeholder.com/300x200"}
        # Додайте інші товари за необхідністю
    ] #Product.query.all()
    return render_template('products.html', items=items)

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
