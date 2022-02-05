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
def read_player():
    players = Player.query.all()
    players_response = []
    for player in players:
        players_response.append(player.to_dict())

    return jsonify(players_response)

# POST /players (create player)
@players_bp.route("", methods=["POST"])
def create_player():
    request_body = request.get_json()
    new_player = Player(name=request_body["name"])

    db.session.add(new_player)
    db.session.commit()

    return jsonify(new_player.to_dict())

#DELETE PLAYER 
@players_bp.route("/<player_id>", methods=["DELETE"])
def delete_a_player(player_id):
    player = Player.query.get(player_id)
    if player is None:
        return make_response(f"Player {player_id} not found", 404)
    
    db.session.delete(player)
    db.session.commit()
    return make_response(f'Player {player.player_id} successfully deleted', 200)

#<--------------- #GET POST & DELETE GAMES --------------->
# GET /games - Read game
# 405 Method Not Allowed - When I changed the route to check the games of a certain player
# it worked when the route was just /games but I need it to be specific
# @games_bp.route("/<player_id>/games", methods=["GET"])
# def read_game(player_id):
#     #games = Game.query.all()
#     player = Player.query.get(player_id)

#     if player is None:
#         return make_response("Game not found", 404)

#     games = Game.query.filter(Game.player_id_fk==player_id).all()
#     games_response = []
#     for game in games:
#         games_response.append(game.to_dict())
            
#     return jsonify(games_response, 200)

# POST /players/<player_id>/games - Create game from players id ------WORKS!
@players_bp.route("/game", methods=["POST"])
def post_game_to_player():
    # player = Player.query.get(player_id) 
    challenger_id = request.get_json()['challenger_id']
    responder_id = request.get_json()['responder_id']
    challenger = Player.query.get(player_id=challenger_id) 
    responder = Player.query.get(player_id=responder_id)

    if challenger is None:
        return make_response("Player not found", 404)
    elif responder is None:
        return make_response("Player Not Found", 404)

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

#PUT GAME rating
# @games_bp.route("/<player_id>/<game_id>", methods=["PUT"])
# def update_a_game(game_id):
#     game = Game.query.get(game_id)
    
#     if game is None:
#         return make_response(f"Game {game_id} not found", 404)

#     game.rating_count+=1
#     db.session.commit()
    
#     response = {
#         "game_id": game.game_id,
#         # "rating_count": game.rating_count,
#         "player_id": game.player_id_fk
#     }
#     return make_response(response, 200)