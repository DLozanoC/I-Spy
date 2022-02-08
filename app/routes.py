from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.models import Game
from app.models.models import Player

# example_bp = Blueprint('example_bp', __name__)

#created blueprint variables
games_bp = Blueprint('games_bp', __name__, url_prefix="/games")
players_bp = Blueprint('players_bp', __name__, url_prefix="/players")

#<--------------- #GET & POST PLAYERS --------------->

# GET /players - Read player info
@players_bp.route("", methods=["GET"])
def read_players():
    players = Player.query.all()
    players_response = []
    for player in players:
        players_response.append(player.to_dict())

    return jsonify(players_response)

# Might not be neccessary since google sign in takes care of this for us. DOUBLE CHECK
# POST /players (create player)
@players_bp.route("", methods=["POST"])
def create_player():
    request_body = request.get_json()
    new_player = Player(name=request_body["name"])

    db.session.add(new_player)
    db.session.commit()

    return jsonify(new_player.to_dict())

#DELETE PLAYER - Might not be neccessary <- DOUBLE CHECK
@players_bp.route("/<player_id>", methods=["DELETE"])
def delete_a_player(player_id):
    player = Player.query.get(player_id)
    if player is None:
        return make_response(f"Player {player_id} not found", 404)
    
    db.session.delete(player)
    db.session.commit()
    return make_response(f'Player {player.player_id} successfully deleted', 200)

#<--------------- #GET POST PUT & DELETE GAMES --------------->
# GET /games - Read games from one specific player ----FINISHED!
@games_bp.route("/<player_id>", methods=["GET"])
def read_game(player_id):

    player = Player.query.get(player_id)
    player_name = player.name

    if player is None:
        return make_response("Game not found", 404)

# Empty dict that will be populated with challenger and responder as keys and their games list as values
    dict_responses = {}

# Challenger
    games_challenger = Game.query.filter(Game.challenger_id==player_id).all()
    games_challenger_response = []
    for game in games_challenger:
        game_names = game.to_dict()
        game_names["challenger_name"] = player_name #Adding challenger's name to my games dict
        responder = Player.query.get(game.responder_id) #Calling the responders name from the id 
        game_names["responder_name"] = responder.name #Adding responder's name to my games dict
        games_challenger_response.append(game_names)
    dict_responses["challenger"] = games_challenger_response

# Responder
    games_responder = Game.query.filter(Game.responder_id==player_id).all()
    games_responder_response = []
    for game in games_responder:
        game_names = game.to_dict()
        game_names["responder_name"] = player_name
        challenger = Player.query.get(game.challenger_id)
        game_names["challenger_name"] = challenger.name
        games_responder_response.append(game_names)
    dict_responses["responder"] = games_responder_response

    
    return jsonify(dict_responses, 200)

# GET /game - Read one specific game ---WORKS!
@games_bp.route("/<player_id>/<game_id>", methods=["GET"])
def get_specific_game(player_id, game_id):

    game = Game.query.get(game_id)

    if game is None:
        return make_response("Game not found", 404)
    
    return game.to_dict(), 200


# POST /players/game - Create game ------WORKS!
@players_bp.route("/game", methods=["POST"])
def post_game_to_player():
    # player = Player.query.get(player_id) 
    challenger_id = request.get_json()['challenger_id']
    responder_id = request.get_json()['responder_id']
    challenger = Player.query.get(challenger_id) 
    responder = Player.query.get(responder_id)

# HOW TO ADD THE NAME OF THE PLAYER INSTEAD OF JUST PRINTING "PLAYER NOT FOUND"
# MCOME UP WITH A BETTER RESPONSE
    if challenger is None:
        return make_response("Player not found", 404)
    elif responder is None:
        return make_response("Player Not Found", 404)
    elif challenger == responder:
        return make_response("You can't play a game with yourself", 405)
#In the body I need the challenge (needs to be saved with the game entity)
    request_body = request.get_json()
    new_game = Game(challenger_id=challenger_id, responder_id=responder_id) 
    # I could call the player by name instead of id

    db.session.add(new_game)
    db.session.commit()

    return make_response(f"Game {new_game.game_id} successfully created", 201)

#DELETE /games/<game_id> -----WORKS!
# Can I change it so the route includes the player id? Maybe it won't work like the GET for games
# @games_bp.route("/<game_id>", methods=["DELETE"])
# def delete_a_game(game_id):
#     game = Game.query.get(game_id)
#     if game is None:
#         return make_response(f"Game {game_id} not found", 404)
    
#     db.session.delete(game)
#     db.session.commit()
#     return make_response(f'Game {game.game_id} successfully deleted', 200)

#PUT GAME rating --- Working on this
# @games_bp.route("/<player_id>/<game_id>/text", methods=["PUT"])
# def rate_friend(player_id, game_id):
#     game = Game.query.get(game_id)
#     # player = Player.query.get(player_id)
#     # challenger = Game.query.filter(Game.challenger_id==player_id)
#     request_body = request.get_json()

#     if game is None:
#         return make_response(f"Game {game_id} not found, can't send your message", 404)
#     #Do I need to add if challenger is None?
    
#     response = {
#         "text_challenger": game.text_challenger,
#     }

#     game.text_challenger = request_body["text_challenger"]

#     db.session.commit()

#     return make_response(response, 200)