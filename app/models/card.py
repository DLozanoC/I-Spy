from app import db

class Card(db.Model):
    __tablename__= 'card'
    card_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)


# Card, table name: card
# card_id, int, primary key
# message, string
# likes_count, int