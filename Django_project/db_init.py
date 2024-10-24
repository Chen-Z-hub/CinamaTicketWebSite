from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from setting import SQLALCHEMY_DATABASE_URI
from flask_cors import CORS
app = Flask(__name__)
# 允许跨域传输数据
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
from flask import Flask 
from flask_cors import CORS
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, methods=["GET", "POST", "PUT", "DELETE"], headers=["Content-Type", "Authorization"])
