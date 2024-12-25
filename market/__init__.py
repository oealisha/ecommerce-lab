from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///../market/instance/market.db"
db = SQLAlchemy(app)

from market import routes


# Use application context for database inspection
# with app.app_context():
#     # Inspect all tables
#     inspector = inspect(db.engine)
#     print("Tables in the database:", inspector.get_table_names())

#     # Inspect the 'item' table schema
#     columns = inspector.get_columns('item')
#     for column in columns:
#         print(f"Column: {column['name']}, Type: {column['type']}, Nullable: {column['nullable']}")