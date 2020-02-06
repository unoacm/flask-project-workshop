from app import app, models, db
from app.forms import SignupForm, LoginForm
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, current_user

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
        return redirect(url_for('index'))
    else:
        return render_template('login.html', title='Sign In', form=form)

