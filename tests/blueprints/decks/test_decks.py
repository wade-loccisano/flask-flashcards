from main import app


def test_get_all_decks():
    with app.test_client() as c:
        response = c.get("/decks")
        # print(response.data)
        assert response.status_code == 200


def test_get_all_decks_endpoint():
    with app.test_client() as c:
        response = c.get("/api/DecksApiEndpoint")
        json_response = response.get_json()
        assert json_response == {"message": "this is a respons from the get request"}
        assert response.status_code == 200
