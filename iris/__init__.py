from flask import Flask

# Create app
app = Flask(__name__)

# Because the import of the routes relies on the app being present we import
# them after creating the app
from iris import routes
