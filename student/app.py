from flask import Flask
from flask_session import Session
from models import db, bcrypt
from routes import register_routes

app = Flask(__name__)

# 🔹 MySQL Configuration (Replace with your Laravel database credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user1:paul1234@localhost/clinicDB'
app.config['SECRET_KEY'] = 'paul1234'
app.config['SESSION_TYPE'] = 'filesystem'

# 🔹 Initialize Extensions
db.init_app(app)
bcrypt.init_app(app)
Session(app)

# 🔹 Register Routes (Imported from `routes.py`)
register_routes(app)

# 🔹 Create Database Tables (Only needed for first-time setup)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)