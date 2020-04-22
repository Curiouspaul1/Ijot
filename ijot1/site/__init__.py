from flask import Blueprint

sitemod = Blueprint('site', __name__, template_folder='templates')

from . import views