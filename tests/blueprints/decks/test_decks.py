def test_get_all_decks(flask_app):
    response = flask_app.get("/decks")
    print(response.data)
    assert response.status_code == 201
