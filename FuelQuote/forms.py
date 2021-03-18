from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, \
    DateField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from wtforms.fields.html5 import DateField


# Code for the registration form that users will fill out if they want to
# create an account
class RegistrationForm(FlaskForm):
    # Create a username field that requires data to be entered with a
    # minimum of 2 characters and a maximum of 25 characters.
    # An error message will pop up if the requirements are not met
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=25)])
    # Create a password field that requires data to be entered with a
    # minimum of 4 characters. An error message will pop up if the 
    # requirements are not met
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=4)])
    # Create a password confirmation field that requires the password to be 
    # confirmed by the user and this field must be equal to the password field.
    # Otherwise, an error will pop up alerting the user that the passwords do 
    # not match.
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    # A submittion field that will sign the user up
    submit = SubmitField('Sign Up')


# Code for the login form for when a registered user wants to login
class LoginForm(FlaskForm):
    # Username field
    username = StringField('Username', validators=[DataRequired()])
    # Password field
    password = PasswordField('Password', validators=[DataRequired()])
    # Optional remember me button
    remember = BooleanField('Remember me')
    # Login button
    submit = SubmitField('Login')


# A function that checks to make sure that the zip code entered is numerical


# and is between 5 and 9 numbers. If it does not pass those requirements then
# throw a validation error to the user letting them know what they did wrong
def zipCodeCheck(form, field):
    # Check to make sure the data entered is a number and not text
    if field.data.isdigit() == False:
        raise ValidationError('Field must be numerical')
    # Check to make sure the data entered is less than 9 numbers
    if len(field.data) > 9:
        raise ValidationError('Field must be less than 9 numbers')
    # Check to make sure the data entered is greater than 5 numbers
    elif len(field.data) < 5:
        raise ValidationError('Field must be greater than 5 numbers')


# Code for the account information form. Users will be redirected to this
# page after they successfully create an account for the first time
class AccountInfoForm(FlaskForm):
    # Have user  enter their full name with a limit of 50 characters.
    # This field is mandatory to fill out otherwise it will throw an error
    fullName = StringField('Full Name',
                           validators=[DataRequired(), Length(max=50)])
    # Have user  enter their addresss with a limit of 100 characters.
    # This field is mandatory to fill out otherwise it will throw an error
    addressOne = StringField('Address 1',
                             validators=[DataRequired(), Length(max=100)])
    # Have user  enter a second address with a limit of 100 characters
    # This field is optional and will not throw an error if left unfilled
    addressTwo = StringField('Address 2',
                             validators=[Length(max=100)])
    # Have user enter the city that they live in with a limit of 100 characters
    # This field is mandatory to fill out otherwise it will throw an error
    city = StringField('City',
                       validators=[DataRequired(), Length(max=100)])
    # Have user select the state they live in. This field is going to be 
    # filled with dummy data at the moment, but will be filled with 
    # database query values when the backend is implemented. 
    state = SelectField('State',
                        choices=['Alabama', 'Alaska', 'Arizona', 'Arkansas',
                                 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
                                 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Kansas', 'Kentucky',
                                 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
                                 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
                                 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
                                 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
                                 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
                                 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
                                 'West Virginia', 'Wisconsin', 'Wyoming'])
    # Have user enter their zip code. This field is mandatory and only
    # accepts numerical values between 5 and 9 characters.
    zipCode = StringField('Zip Code',
                          validators=[DataRequired(), zipCodeCheck])
    # A submit button to submit information
    submit = SubmitField('Update')


# Code for the login form for when a registered user wants to login
class FuelQuoteForm(FlaskForm):
    # Gallons field
    gallons = IntegerField('Request Gallons', validators=[DataRequired()])
    # Delivery Date field
    # date = DateField('Delivery Date', format="%m/%d/%Y", validators=[DataRequired()])
    date = DateField('Delivery Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    # date = DateField('DatePicker', format='%Y-%m-%d')
    # Quote button
    submit = SubmitField('Quote')
