from market import app
from flask import render_template
from market.models import Item

@app.route('/about/<username>')
def about_page(username):
    return f'<h1> This is the about page of {username}</h1>'

@app.route('/home')
@app.route('/')
def home_page_1():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)