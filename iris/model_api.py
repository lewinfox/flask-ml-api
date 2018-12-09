def make_prediction(model, data):
    species = model.predict([data])[0]
    pred_prob = max(model.predict_proba([data])[0])
    return {"pred_class": species, "pred_prob": pred_prob}
