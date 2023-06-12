from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://geektime_0:geektime_0@mysql.hogwarts.ceshiren.com:3306/geektime_0?charset=utf8mb4"
app.secret_key = 'hogwarts'
app.config["JWT_SECRET_KEY"] = "hogwarts"  # Change this!

app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
# app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False
jwt = JWTManager(app)
CORS(app)
