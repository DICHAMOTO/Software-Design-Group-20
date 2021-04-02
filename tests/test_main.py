import os
import unittest
 
from quote_project import app, db
from quote_project.models import User
 
 
TEST_DB = 'test.db'
 
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        app.config['LOGIN_DISABLED'] = True
        self.app = app.test_client() 
    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_main_page(self):
        response = self.app.get('home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_root_route(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
    def register(self, username, password, confirm):
        return self.app.post(
            '/register',
            data=dict(username=username, password=password, confirm=password),
            follow_redirects=True
        )

    def profilemgmt(self, name, address, city, state, zip_code):
        return self.app.post(
            '/profilemgmt',
            data=dict(name=name, address=address, city=city, state=state, zip_code=zip_code),
            follow_redirects=True
        )
 
    def login(self, username, password):
        return self.app.post(
            '/login',
            data=dict(username=username, password=password),
            follow_redirects=True
        )

    def fuel_quote(self, del_date, gallons):
        return self.app.post(
            '/fuelquote',
            data=dict(del_date=del_date, gallons=gallons),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )
 
    def test_valid_user_registration(self):
        response = self.register('dummydata', 'FlaskIsAwesome', 'FlaskIsAwesome')
        assert response.data is not None
        assert response.status_code == 200

    def test_invalid_user_registration_different_passwords(self):
        response = self.register('dummydata', 'FlaskIsAwesome', 'FlaskIsNotAwesome')
        assert response.data is not None
        assert response.status_code == 200

    def test_invalid_user_registration_duplicate_username(self):
        response = self.register('dummydata', 'FlaskIsAwesome', 'FlaskIsAwesome')
        response = self.register('dummydata', 'FlaskIsReallyAwesome', 'FlaskIsReallyAwesome')
        assert response.data is not None
        assert response.status_code == 200

    def test_login(self):
        response = self.login('dummydata', 'FlaskIsAwesome')
        assert response.data is not None
        assert response.status_code == 200

    def test_profile_mgmt(self):
        response = self.profilemgmt('Brendan Morales', '123 beep blvd', 'houston', 'Texas', '77042')
        assert response.data is not None
        assert response.status_code == 200

    def test_profile_mgmt_large_zip(self):
        response = self.profilemgmt('Brendan Morales', '123 beep blvd', 'houston', 'Texas', '78978978798')
        assert response.data is not None
        assert response.status_code == 200

    def test_fuel_quote(self):
        response = self.fuel_quote('2022-01-01', '50')
        assert response.data is not None
        assert response.status_code == 400

    def test_logout(self):
        response = self.logout()
        assert response.data is not None
        assert response.status_code == 200