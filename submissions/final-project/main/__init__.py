from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from main import routes