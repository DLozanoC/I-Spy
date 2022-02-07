from app import db

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
            }
    
class Player(db.Model):
    __tablename__= 'player'
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    challenger = db.relationship('Game', foreign_keys=[Game.responder_id], backref=db.backref('responder', lazy='joined'), lazy='dynamic')
    responder = db.relationship('Game', foreign_keys=[Game.challenger_id], backref=db.backref('challenger', lazy='joined'), lazy='dynamic')
    
    def to_dict(self):
        return {
            "id": self.player_id,
            #Add email here somehow
            "name": self.name,
        }



