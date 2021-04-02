from flask import render_template, url_for, flash, redirect, request
from quote_project.forms import RegistrationForm, LoginForm, AccountInfoForm, FuelQuoteForm
from quote_project import app, db, bcrypt
from quote_project.models import User, Quote, Profile
from flask_login import current_user, login_required, login_user, logout_user
import json


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
        # if form.username.data == 'moto' and form.password.data == 'testing':
        # flash(f'You have been logged in! Welcome {form.username.data}! Please complete your profile.', 'success')
        # return redirect(url_for('profileManagement'))
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Howdy {form.username.data}! Now redirecting you to finish your profile.', 'success')
            return redirect(next_page) if next_page else redirect(url_for('profileManagement'))
        else:
            flash(f'Login Unsuccessful. Please check username or password.', 'danger')
    return render_template('login.html', title='Login', form=form)


# Method for profile management
@app.route("/profilemgmt", methods=['GET', 'POST'])
@login_required
def profileManagement():
    # # Instantiate the account information form
    form = AccountInfoForm()
    # If all fields are correctly filled out, then flash success message
    if form.validate_on_submit():
        flash(f'{form.fullName.data} your account information has been successfully updated',
              'success')

        exist = db.session.query(db.exists().where(Profile.user_id == current_user.id)).scalar() # check if this is exist in profile table

        if exist: #modify
            prof = db.session.query(Profile).filter(Profile.user_id == current_user.id).first()
            prof.fullname = form.fullName.data
            prof.address1 = form.addressOne.data
            prof.address2 = form.addressTwo.data
            prof.city = form.city.data
            prof.state = form.state.data
            prof.zip = form.zipCode.data

        else:  # the profile of currentuser not exist     
            profileEntry = Profile(user_id = current_user.id, fullname = form.fullName.data, address1 = form.addressOne.data,
            address2 = form.addressTwo.data, city = form.city.data, state = form.state.data, zip = form.zipCode.data)
            print(profileEntry)
            # add row to db commitment
            db.session.add(profileEntry)

        # push to the db
        db.session.commit()
    return render_template('account.html', title="Profile Management",
                           form=form)


@app.route('/fuelquote', methods=['GET', 'POST'])
@login_required
def fuelquote():
    form = FuelQuoteForm()
    if request.method == 'POST':
        if request.form['submit_button'] == 'Calculate Total':
            print("you press the calculate button!!!")
            return render_template('fuelquote.html', title='Fuel Quote', form=form)
        elif request.form['submit_button'] == 'Quote':
            print("you press the quote button!!!")
            user_id = current_user.id
            profile_id = Profile.query.filter_by(user_id=user_id).first().id
            delivery_date = form.date.data
            request_gallons = form.gallons.data
            suggested_price = form.price
            total = request_gallons * suggested_price
            quote = Quote(delivery_date=delivery_date, request_gallons=request_gallons, suggested_price=suggested_price,
                          user_id=user_id, total=total, profile_id=profile_id)
            db.session.add(quote)
            db.session.commit()
            flash(f'Quote!',
                  'success')
    return render_template('fuelquote.html', title='Fuel Quote', form=form)


@app.route("/history")
def display_history():
    # count the # of row in Quote table:
    numRow = Quote.query.count()
    quote_records = []
    # create empty dictionary:
    for counter in range(1, numRow+1):
        client_name = Quote.query.filter_by(id=counter).first().profile.fullname
        gallons_requested = Quote.query.filter_by(id=counter).first().request_gallons
        delivery_address1 = Quote.query.filter_by(id=counter).first().profile.address1
        delivery_address2 = Quote.query.filter_by(id=counter).first().profile.address2
        if delivery_address2 is None:
            delivery_address2 = ""
        zipcode = Quote.query.filter_by(id=counter).first().profile.zip
        city = Quote.query.filter_by(id=counter).first().profile.city
        state = Quote.query.filter_by(id=counter).first().profile.state
        # concate address:
        delivery_address = f'{delivery_address1} {delivery_address2}, {city}, {state}, {zipcode}'
        delivery_date = Quote.query.filter_by(id=counter).first().delivery_date
        suggested_price = Quote.query.filter_by(id=counter).first().suggested_price
        total_amount = Quote.query.filter_by(id=counter).first().total
        quote_created = Quote.query.filter_by(id=counter).first().date_quoted
        temp_dict = {'client_name': client_name,
                     'gallons_requested': gallons_requested,
                     'delivery_address': delivery_address,
                     'delivery_date': delivery_date,
                     'suggested_price': f'${suggested_price}',
                     'total_amount': f'${total_amount}',
                     'quote_created': quote_created
                     }
        quote_records.append(temp_dict)
    print(quote_records)
    return render_template('history.html', title='History', histories=quote_records)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
