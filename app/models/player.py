from app import db

# ASSOCIATION TABLE to connect players and games
player_game = db.table('player_game',
db.Column('player_id',db.ForeignKey('player.player_id')),
db.Column('game_id', db.Integer, db.ForeignKey('game.game_id')))

class Player(db.Model):
    __tablename__= 'player'
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # games = db.relationship('Game', backref='player')
    #board_id_fk = db.Column(db.Integer, db.ForeignKey('board.board_id'), nullable=True)

    def to_dict(self):
        return {
            "id": self.player_id,
            "name": self.name,
        }



