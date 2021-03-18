import os
from flask import Flask


# app = Flask(__name__)
#
#
# app.config['SECRET_KEY'] = '788270a3a29cf81029ca3a09528ff90a'

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # register the database
    from FuelQuote import db

    db.init_app(app)

    # apply the blueprint to the app
    from FuelQuote import auth
    app.register_blueprint(auth.bp)

    return app
