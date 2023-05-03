from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sys_eye_id.db"
app.config["SECRET_KEY"] = "6f03ee85b143f1a78a74bef70f7d3303"
app.config["UPLOAD_FOLDER"] = "static/exames"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

from SysEyeId import routes