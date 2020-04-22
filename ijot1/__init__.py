from flask import Flask
from .extensions import ma,db,mail,bcrypt
from config import config

def __call__(config_object):
    app = Flask(__name__)
    app.config.from_object(config[config_object])

    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)

    # import blueprint
    from ijot1.site.views import sitemod
    #from ijot1.api.views import apimod

    # register blueprint
    app.register_blueprint(site.views.sitemod)
    #app.register_blueprint(api.views.apimod,url_prefix='/api')

    return app