from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    reg = request.form["reg"]
    phone = request.form.get('phone', '')  # Optional field
    user = User(name=name, email=email, reg=reg, phone=phone)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
