# from app import db

# class Message(db.Model):
#     __tablename__= 'message'
#     message_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String)
#     sender = db.Column(db.String) #would this be the relationship
#     player_id_fk = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=True)
#     game_id_fk = db.Column(db.Integer, db.ForeignKey('game.game_id'), nullable=True)
#     #time = db.Column
#     #receiver = db.Column
#     #make sure this is a many to many relationship. Cards should be "player"
#     #cards = db.relationship('Card', backref='message')


#     def to_dict(self):
#         return {"message_id": self.message_id,
#             "title": self.title,
#             "owner": self.owner,
#             # "cards":[card.to_dict() for card in self.cards],
#             }


#tasks = db.relationship('Task', backref='goal', lazy=True)