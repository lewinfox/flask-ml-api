import os
from flask import Flask, render_template, request
from flask.json import jsonify
import pickle
import numpy as np


# Function to handle model prediction
def make_prediction(model, data):
    species = model.predict([data])[0]
    pred_prob = max(model.predict_proba([data])[0])
    return {"pred_class": species, "pred_prob": pred_prob}


# Load the picked model
with open("model/iris.pickle", "rb") as f:
    model = pickle.load(f)

# Create app
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run()
