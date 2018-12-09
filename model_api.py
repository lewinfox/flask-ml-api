import numpy as np
def make_prediction(model, data):
    species = model.predict([data])[0]
    pred_probs = list(model.predict_proba([data])[0])
    return {"pred_class": species, "pred_probs": pred_probs}
