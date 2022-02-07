from app import db

# ASSOCIATION TABLE to connect players and games
# player_game = db.table('player_game',
# db.Column('player_id',db.Integer, db.ForeignKey('player.player_id')),
# db.Column('game_id', db.Integer, db.ForeignKey('game.game_id')))

class Game(db.Model):
    __tablename__= 'game'
    game_id = db.Column(db.Integer, primary_key=True)
    # rating_count = db.Column(db.Integer)#Change to string 
    #add challenger text and responder text
    challenger_id = db.Column(db.Integer, db.ForeignKey('player.player_id'))
    responder_id = db.Column(db.Integer, db.ForeignKey('player.player_id'))

    def to_dict(self):
        return {"game_id": self.game_id,
        "challenger_id": self.challenger_id,
        "responder_id": self.responder_id
            #"player": self.player_id_fk,
            }
    
class Player(db.Model):
    __tablename__= 'player'
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    challenger = db.relationship('Game', foreign_keys=[Game.responder_id], backref=db.backref('responder', lazy='joined'), lazy='dynamic')
    responder = db.relationship('Game', foreign_keys=[Game.challenger_id], backref=db.backref('challenger', lazy='joined'), lazy='dynamic')
    #player_game = db.relationship('Game', secondary=player_game, backref='player', lazy='select')
# Only to use when I have an association table
    def to_dict(self):
        return {
            "id": self.player_id,
            #Add email here somehow
            "name": self.name,
        }



