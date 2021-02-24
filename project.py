from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, AccountInfoForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '788270a3a29cf81029ca3a09528ff90a'

# Temporary JSON structures for the history page input
quote_histories = [
    {
        'client_name': 'Sheila W Koga',
        'gallons_requested': '5000',
        'delivery_address': '1989 Scenic Way, Champaign, Illinois(IL), 61820',
        'delivery_date': '03-01-2021',
        'suggested_pice': '$2.05',
        'total_amount': '$10250',
        'quote_created': '02-23-2021'
    },
    {
        'client_name': 'William E Walker',
        'gallons_requested': '2500',
        'delivery_address': '263 Snowbird Lane, Omaha, Nebraska(NE), 68114',
        'delivery_date': '02-28-2021',
        'suggested_pice': '$1.95',
        'total_amount': '$4875',
        'quote_created': '02-21-2021'
    },
    {
        'client_name': 'Robert G Ferreira',
        'gallons_requested': '10500',
        'delivery_address': '673 Cross Street, Saginaw, Michigan(MI), 48601',
        'delivery_date': '04-23-2021',
        'suggested_pice': '$3.00',
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
    return render_template('about.html', title = 'About')

# Method for the registration page
# 'GET' and 'POST' methods for get and post requests
@app.route("/register", methods = ['GET', 'POST'])
def register():
	# Instantiate a registration form
	form = RegistrationForm()
	# If account is created successfully then flash a message letting the 
	# user know that their account was created and redirect them to 
	# the profile management page so they can fill out account information
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title = 'Register', form = form)

# Method for the login page
@app.route("/login", methods = ['GET', 'POST'])
def login():
	# Instantiate a login form and take user to the login page
	form = LoginForm()
	# If login is successful, then flash a message to the user that their login
	# was successful.
	# If the login is unsuccessful, then flash a message that the username or
	# password is incorrect.
	if form.validate_on_submit():
		# This username and password data is just dummy data to test out 
		# login functionality. Will be deleted in future.
		if form.username.data == 'moto' and form.password.data == 'testing':
			flash(f'You have been logged in! Welcome {form.username.data}!', 'success')
			return redirect(url_for('profileManagement'))
		else:
			flash(f'Login Unsuccessful. Please check username or password.' ,'danger')
	return render_template('login.html', title = 'Login', form = form)

# Method for profile management
@app.route("/profilemgmt", methods = ['GET', 'POST'])
def profileManagement():
	# Instantiate the account information form
	form = AccountInfoForm()
	# If all fields are correctly filled out, then flash success message
	if form.validate_on_submit():
		flash(f'{form.fullName.data} your account information has been successfully updated',
		 'success')
	return render_template('account.html', title = "Account", 
		form = form)


@app.route("/history")
def display_history():
    return render_template('history.html', title='History', histories=quote_histories)


if __name__ == '__main__':
    app.run(debug=True)