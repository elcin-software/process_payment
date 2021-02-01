from typing import Any
from flask import Flask
from application import format


def createApp(config_object="application.configuration"):
	app = Flask(__name__)
	app.config.from_object(config_object)
	register_blueprints(app)
	return app


def register_blueprints(app):
	app.register_blueprint(format.format.blueprint)
	return None
