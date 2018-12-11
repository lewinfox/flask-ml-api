from iris import app
from flask.json import jsonify
from flask import render_template, request
from model import model, make_prediction

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
        input_data = [x for x in data.values()]
        print(f"input_data: {input_data}")
        result = make_prediction(model, input_data)
        return jsonify(result)
    except Exception as e:
        print(e)
