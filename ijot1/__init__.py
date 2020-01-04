from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate,MigrateCommand
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# session key
app.secret_key = os.urandom(24)

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)

# import blueprint
from ijot1.site.views import sitemod
from ijot1.api.views import apimod

# register blueprint
app.register_blueprint(site.views.sitemod)
app.register_blueprint(api.views.apimod,url_prefix='/api')