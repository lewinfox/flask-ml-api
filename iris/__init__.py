from flask import Flask

# Create app
app = Flask(__name__)

# Because the import of the routes relies on the app being present
from iris import routes
