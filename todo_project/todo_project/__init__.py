import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from prometheus_flask_exporter import PrometheusMetrics

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///" + os.path.join(basedir, "site.db"))
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key") 

metrics = PrometheusMetrics(app)

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "danger"

bcrypt = Bcrypt(app)

# Always put Routes at end
from todo_project import routes
