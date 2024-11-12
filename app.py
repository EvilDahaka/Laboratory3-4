from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(73), nullable=False)
    description = db.Column(db.String(178), nullable=False)
    price = db.Column(db.Float, nullable=False) 
    image_url = db.Column(db.String(200), nullable=False)

class feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(54), nullable=False)
    description = db.Column(db.String(500), nullable=False)



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    tag = request.args.get('tag')  # Отримуємо тег із параметрів запиту
    if tag:
        items = Product.query.filter_by(tag=tag).all()  # Фільтруємо за тегом
    else:
        items = Product.query.all()
    return render_template('products.html', items=items)
@app.route('/product/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        tag = request.form['tag']
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        image_url = request.form['image_url']

        # Створюємо новий об'єкт Product та додаємо його в базу
        new_product = Product(tag=tag, name=name, description=description, price=float(price), image_url=image_url)
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('products'))
    
    return render_template('add_product.html')

@app.route('/feedback')
def feedback():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        description = request.form['description']

        new_feedback = feedback(email=email, name=name, description=description,)
        db.session.add(new_feedback)
        db.session.commit()

        return redirect(url_for('feedback'))
    return render_template('feedback.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
