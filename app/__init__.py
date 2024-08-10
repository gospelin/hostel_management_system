from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
#from flask_admin import Admin
from config import config_by_name, os
#from .authentication import login_manager

# Initialize the app
app = Flask(__name__)

# Load configuration based on the environment
env = os.getenv("FLASK_ENV", "default")
app.config.from_object(config_by_name[env])

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#csrf = CSRFProtect(app)

from app import routes
