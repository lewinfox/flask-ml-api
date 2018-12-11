import pickle

# Load the picked model
with open("model/iris.pickle", "rb") as f:
    model = pickle.load(f)
