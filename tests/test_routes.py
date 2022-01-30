
#Client is the testing version of our Flask App
def test_get_all_players(client):
    #Act
    response = client.get("/players")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

# def test_create_player(client):
#     #Act
#     response = client.post("/players")
#     response_body = response.get_json()

#     #Assert
#     assert response.status_code == 200
#     assert response_body == []

#Get players with name
def test_get_all_players_with_name(client, create_players):
    #Act
    response = client.get("/players")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    