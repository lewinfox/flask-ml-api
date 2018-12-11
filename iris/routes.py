from iris import app
from flask.json import jsonify
from flask import render_template, request
from model import model
from model.model_api import make_prediction

# define routes
@app.route("/")
@app.route("/index")
def index():
    """Serve the application's main page."""

    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    """Obtain a prediction from the model.

    The intention is that this function should need little to no modification
    to work with different models. Its only purpose is to collect the
    data from the POST request, pass it to the model's `make_prediction`
    function, and return the output of that function to the client. All
    data processing should be handled by `model.make_prediction`.

    Note that it returns the data in JSON format - is it assumed that we are
    working with AJAX requests. If the client is not expecting an AJAX response
    the raw JSON should still be displayed.

    What the browser does with the response is also not specified here - write
    your own JavaScript function at the other end.
    """
    try:
        data = request.form
        result = make_prediction(model, data)
        return jsonify(result)
    except Exception as e:
        print(e)  # TODO: Make this nicer
