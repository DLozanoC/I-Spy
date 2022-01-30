from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.game import Game
# from app.models.message import Message
from app.models.player import Player

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

#<--------------- #GET POST & DELETE GAMES --------------->
# GET /games - Read game
@games_bp.route("", methods=["GET"])
def read_game():
    games = Game.query.all()
    games_response = []
    for game in games:
        games_response.append(game.to_dict())
            
    return jsonify(games_response)

# POST /players/<player_id>/games - Create game from players id
@players_bp.route("/<player_id>/games", methods=["POST"])
def post_game_to_player(player_id):
    player = Player.query.get(player_id) 

    if player is None: #error checking
        return make_response("Player Not Found", 404)

    request_body = request.get_json()
    new_game = Game(game_id=request_body["game_id"],
        player_id_fk=player.player_id) #this may raise error

    db.session.add(new_game)
    db.session.commit()

    return make_response(f"Game {new_game.game_id} successfully created", 201)

#DELETE /games/<game_id>
@games_bp.route("/<game_id>", methods=["DELETE"])
def delete_a_game(game_id):
    game = Game.query.get(game_id)
    if game is None:
        return make_response(f"Game {game_id} not found", 404)
    
    db.session.delete(game)
    db.session.commit()
    return make_response(f'Game {game.game_id} successfully deleted', 200)

#PUT GAME rating
@games_bp.route("/<game_id>/rating", methods=["PUT"])
def update_a_game(game_id):
    game = Game.query.get(game_id)
    
    if game is None:
        return make_response(f"Game {game_id} not found", 404)

    game.rating_count+=1
    db.session.commit()
    
    response = {
        "game_id": game.game_id,
        "rating_count": game.rating_count,
        "player_id": game.player_id_fk
    }
    return make_response(response, 200)