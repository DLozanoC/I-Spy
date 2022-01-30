from app import db

class Game(db.Model):
    __tablename__= 'game'
    game_id = db.Column(db.Integer, primary_key=True)
    rating_count = db.Column(db.Integer)
    player_id_fk = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=True)

    #receiver = db.Column
    #make sure this is a many to many relationship. Cards should be "player"
    #cards = db.relationship('Card', backref='message')


    def to_dict(self):
        return {"game_id": self.game_id,
            "player": self.player_id_fk,
            # "cards":[card.to_dict() for card in self.cards],
            }


#tasks = db.relationship('Task', backref='goal', lazy=True)
#SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/inspiration_board_development