
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Initialize CORS
CORS(app)

# Initialize Talisman for Security Headers
talisman = Talisman(app)

from service import routes, models
