import os
from flask import Flask, render_template, request
from flask.json import jsonify
import pickle
from iris.model_api import make_prediction
import numpy as np

with open("iris/model/iris/iris.pickle", "rb") as f:
    model = pickle.load(f)

def create_app(test_config=None):
    # Create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
    SECRET_KEY = "dev"
    )

    # Show instance folder
    print (app.instance_path)

    if test_config is None:
        # load instance config, if there is one, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load test config if passed in
        app.config.from_mapping(test_config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # define routes
    @app.route("/")
    @app.route("/index")
    def index():
        return render_template("index.html")

    @app.route("/predict", methods=["POST"])
    def predict():
        try:
            print(request.form)
            data = {
                "sepal_length": request.form.get("sepal-length"),
                "sepal_width": request.form.get("sepal-width"),
                "petal_length": request.form.get("petal-length"),
                "petal_width": request.form.get("petal-width")
            }
            input_data = np.array([x for x in data.values()])
            print(f"input_data: {input_data}")
            result = make_prediction(model, input_data)
            return jsonify(result)
        except Exception as e:
            print(e)

    return app
