from quote_project import app
import pytest

def test_registration():
	client = app.test_client()

	return client.post('/register', data = dict(
		username = "something",
		password = "testing",
		confirm_password = "testing"
		), follow_redirects = True)

def test_registration_nonmatching_passwords():
	client = app.test_client()

	return client.post('/register', data = dict(
		username = "something",
		password = "testing",
		confirm_password = "te"
		), follow_redirects = True)

def test_registration_missing_passwords():
	client = app.test_client()

	return client.post('/register', data = dict(
		username = "something",
		password = "",
		confirm_password = ""
		), follow_redirects = True)

def test_registration_missing_confirmation_passwords():
	client = app.test_client()

	return client.post('/register', data = dict(
		username = "something",
		password = "testing",
		confirm_password = ""
		), follow_redirects = True)

def test_registration_missing_initial_passwords():
	client = app.test_client()

	return client.post('/register', data = dict(
		username = "something",
		password = "",
		confirm_password = "testing"
		), follow_redirects = True)

def test_login():
    client = app.test_client()

    return client.post('/login', data = dict(
        username = "moto",
        password = "testing"
        ), follow_redirects = True)

def test_login_missing_username():
    client = app.test_client()

    return client.post('/login', data = dict(
        username = "",
        password = "testing"
        ), follow_redirects = True)

def test_login_missing_password():
    client = app.test_client()

    return client.post('/login', data = dict(
        username = "moto",
        password = ""
        ), follow_redirects = True)

def test_profilemgmt():
	client = app.test_client()

	return client.post('/profileSmgmt', data = dict(
		fullName = "Brendan Morales",
		addressOne = "1234 Anderson Blvd",
		city = "Houston",
		state = "Texas",
		zipCode = 77042
		), follow_redirects = True)

def test_invalid_zip_code_large():
	client = app.test_client()

	return client.post('/profileSmgmt', data = dict(
		fullName = "Brendan Morales",
		addressOne = "1234 Anderson Blvd",
		city = "Houston",
		state = "Texas",
		zipCode = 77042321321
		), follow_redirects = True)

def test_invalid_zip_code_small():
	client = app.test_client()

	return client.post('/profileSmgmt', data = dict(
		fullName = "Brendan Morales",
		addressOne = "1234 Anderson Blvd",
		city = "Houston",
		state = "Texas",
		zipCode = 7
		), follow_redirects = True)

def test_invalid_address():
	client = app.test_client()

	return client.post('/profileSmgmt', data = dict(
		fullName = "Brendan Morales",
		addressOne = "",
		city = "",
		state = "Texas",
		zipCode = 7
		), follow_redirects = True)

def test_invalid_name():
	client = app.test_client()

	return client.post('/profileSmgmt', data = dict(
		fullName = "",
		addressOne = "1234 Anderson Blvd",
		city = "Houston",
		state = "Texas",
		zipCode = 7
		), follow_redirects = True)

def test_fuelQuoteForm():
	client = app.test_client()

	return client.post('/fuelquote', data = dict(
		gallons = 50,
		date = "03/21/2021"
		), follow_redirects = True)