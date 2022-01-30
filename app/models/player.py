from app import db

class Player(db.Model):
    __tablename__= 'player'
    player_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    games = db.relationship('Game', backref='player')
    #board_id_fk = db.Column(db.Integer, db.ForeignKey('board.board_id'), nullable=True)

    def to_dict(self):
        return {
            "id": self.player_id,
            "name": self.name,
        }



