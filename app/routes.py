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
    
    if phone:  # Only validate if phone is provided (since it's optional)
        if not phone.isdigit() or len(phone) != 10:
            flash("Phone number must be numeric and exactly 10 digits long.", "error")
            return redirect(url_for('index'))
            
    try:
        user = User(name=name, email=email, reg=reg, phone=phone)
        db.session.add(user)
        db.session.commit()
        flash("User registered successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"An error occurred: {str(e)}", "error")
        
    return redirect(url_for('index'))
