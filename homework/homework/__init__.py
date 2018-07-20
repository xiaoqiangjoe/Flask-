from flask import Flask
from .views.login import log
from .views.index import ind





def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.Config')
    app.register_blueprint(log)
    app.register_blueprint(ind)


    return app




