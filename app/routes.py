from app import app, models, db
from app.forms import SignupForm
from flask import render_template, flash, redirect, url_for

# first route
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# sign-up route: this uses the signup form
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = models.User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)
