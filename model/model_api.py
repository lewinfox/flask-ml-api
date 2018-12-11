# -*- coding: utf-8 -*-
"""API for interacting with sklean model.

Contains a function for obtaining a prediction in the desired format from a
predetermined sklearn iris classification model.
"""

import numpy as np


def make_prediction(model, data):
    """Predict class from input data

    Calls `model.predict()` on `data`.

    Args:
        model (model): A pretrained sklearn model.
        data (list): A list of parameters to be passed to `model`.

    Returns:
        dict: A dictionary containing the predicted species (`pred_class`) and
        prediction confidence (`pred_prob`).
    """

    data_dict = {
        "sepal_length": data.get("sepal-length"),
        "sepal_width": data.get("sepal-width"),
        "petal_length": data.get("petal-length"),
        "petal_width": data.get("petal-width")
    }
    input_data = [x for x in data_dict.values()]
    data = np.array(input_data)
    species = model.predict([input_data])[0]
    pred_prob = max(model.predict_proba([input_data])[0])
    return {"pred_class": species, "pred_prob": pred_prob}
