import pickle

def test_model_files_exist():

    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("model/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    assert model is not None
    assert vectorizer is not None
