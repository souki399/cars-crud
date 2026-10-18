def test_whitespace_is_trimmed_in_the_api_response(client):
    payload = {
        "make": "  Toyota  ",
        "model": " Corolla ",
        "year": 2024,
        "color": " Silver ",
    }

    response = client.post("/api/cars", json=payload)

    assert response.status_code == 201

    body = response.json()

    assert body["make"] == "Toyota"
    assert body["model"] == "Corolla"
    assert body["color"] == "Silver"
