from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)

@app.route('/')
def dashboard():
    categories = Category.query.all()
    expenses = Expense.query.all()
    return render_template('dashboard.html', categories=categories, expenses=expenses)

@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('category_form.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    categories = Category.query.all()
    if request.method == 'POST':
        category_id = request.form['category']
        amount = request.form['amount']
        expense = Expense(category_id=category_id, amount=amount)
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('expense_form.html', categories=categories)

if __name__ == '__main__':
    # Create all database tables if they do not exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
