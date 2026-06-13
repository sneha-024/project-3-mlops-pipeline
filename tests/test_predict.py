from app import app

def test_predict_endpoint():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={"text": "I love this product"}
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "sentiment" in data
    assert "confidence" in data


def test_predict_without_text():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={}
    )

    assert response.status_code == 400
