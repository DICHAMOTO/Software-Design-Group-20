from flask import render_template, url_for, flash, redirect, request
from quote_project.forms import RegistrationForm, LoginForm, AccountInfoForm, FuelQuoteForm
from quote_project import app, db, bcrypt
from quote_project.models import User, Quote, Profile
from flask_login import current_user, login_required, login_user, logout_user
# Songwen's Dummy Temporary JSON structures for the history page input
quote_histories = [
    {
        'client_name': 'Sheila W Koga',
        'gallons_requested': '5000',
        'delivery_address': '1989 Scenic Way, Champaign, Illinois(IL), 61820',
        'delivery_date': '03-01-2021',
        'suggested_price': '$2.05',
        'total_amount': '$10250',
        'quote_created': '02-23-2021'
    },
    {
        'client_name': 'William E Walker',
        'gallons_requested': '2500',
        'delivery_address': '263 Snowbird Lane, Omaha, Nebraska(NE), 68114',
        'delivery_date': '02-28-2021',
        'suggested_price': '$1.95',
        'total_amount': '$4875',
        'quote_created': '02-21-2021'
    },
    {
        'client_name': 'Robert G Ferreira',
        'gallons_requested': '10500',
        'delivery_address': '673 Cross Street, Saginaw, Michigan(MI), 48601',
        'delivery_date': '04-23-2021',
        'suggested_price': '$3.00',
        'total_amount': '$31500',
        'quote_created': '01-31-2021'
    }
]


# Method for the home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


# Method for the about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')


# Method for the registration page
# 'GET' and 'POST' methods for get and post requests
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # Instantiate a registration form
    form = RegistrationForm()
    # If account is created successfully then flash a message letting the
    # user know that their account was created and redirect them to
    # the profile management page so they can fill out account information
    if form.validate_on_submit():
        # hash the user password for higher security level
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # create instance of user model and store name and hashed_password in it
        user = User(username=form.username.data, password=hashed_password)
        # add new user to the database
        db.session.add(user)
        db.session.commit()
        flash(f'Dear {form.username.data}, you account has been successfully created! Please Login on this page.', \
              'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# Method for the login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # Instantiate a login form and take user to the login page
    form = LoginForm()
    # If login is successful, then flash a message to the user that their login
    # was successful.
    # If the login is unsuccessful, then flash a message that the username or
    # password is incorrect.
    if form.validate_on_submit():
        # This username and password data is just dummy data to test out
        # login functionality. Will be deleted in future.
        #if form.username.data == 'moto' and form.password.data == 'testing':
            #flash(f'You have been logged in! Welcome {form.username.data}! Please complete your profile.', 'success')
            #return redirect(url_for('profileManagement'))
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username or password.', 'danger')
    return render_template('login.html', title='Login', form=form)


# Method for profile management
@app.route("/profilemgmt", methods=['GET', 'POST'])
@login_required
def profileManagement():
    # Instantiate the account information form
    form = AccountInfoForm()
    # If all fields are correctly filled out, then flash success message
    if form.validate_on_submit():
        flash(f'{form.fullName.data} your account information has been successfully updated',
              'success')
    return render_template('account.html', title="Profile Management",
                           form=form)


@app.route('/fuelquote', methods=['GET', 'POST'])
@login_required
def fuelquote():
    form = FuelQuoteForm()
    if form.validate_on_submit():
        flash(f'quoted!', 'success')
    return render_template('fuelquote.html', title='Fuel Quote', form=form)


@app.route("/history")
@login_required
def display_history():
    return render_template('history.html', title='History', histories=quote_histories)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))