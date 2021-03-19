from quote_project import app
import pytest

def test_registration():
	client = app.test_client()

	return client.post('/register', data = dict(
		username = "something",
		password = "testing",
		confirm_password = "testing"
		), follow_redirects = True)

def test_login():
    client = app.test_client()

    return client.post('/login', data = dict(
        username = "moto",
        password = "testing"
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

def test_fuelQuoteForm():
	client = app.test_client()

	return client.post('/fuelquote', data = dict(
		gallons = 50,
		date = "03/21/2021"
		), follow_redirects = True)