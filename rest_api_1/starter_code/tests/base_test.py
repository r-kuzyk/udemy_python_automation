from unittest import TestCase
from app import app
from db import db

class BaseTest(TestCase):
    def setUp(self):
        # make sure database exist
        app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # get a test cklient
        pass

    def tearDown(self):
        # make sure database is blunk
        with app.app_context():
            db.session.remove()
            db.drop_all()