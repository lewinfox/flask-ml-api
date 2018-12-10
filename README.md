# flask-ml-api

Building a basic web UI for a sklearn model. Allows a user to input data into a classification model (random forest) based on the iris dataset. Uses AJAX to query the model and display the result.

Also contains the iris dataset and a Jupyter notebook for training and pickling the model.

To run:
* `export FLASK_APP=iris`
* `export FLASK_ENV=development`
* `flask run` or `python run.py`
