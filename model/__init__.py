import pickle
import numpy as np

# Load the picked model
with open("model/iris.pickle", "rb") as f:
    model = pickle.load(f)

# Function to handle model prediction
def make_prediction(model, data):
    data = np.array(data)
    species = model.predict([data])[0]
    pred_prob = max(model.predict_proba([data])[0])
    return {"pred_class": species, "pred_prob": pred_prob}
