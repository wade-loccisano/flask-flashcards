from app.extensions import db
from .__mixins__ import TimestampMixin
from flask_restful import fields


class Card(db.Model, TimestampMixin):
    __tablename__ = "Cards"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # uuid
    front = db.Column(db.String, nullable=False)
    back = db.Column(db.String, nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey("Decks.id"))
    deck = db.relationship("Deck", back_populates="cards")

    def __init__(self, front, back, deck_id):
        self.front = front
        self.back = back
        self.deck_id = deck_id

    def __repr__(self):
        return "Deck(front='{}', back='{}', deck_id='{}')".format(
            self.front,
            self.back,
            self.deck_id,
        )

    def serialize(self):
        return {
            "id": self.id,
            "front": self.front,
            "back": self.back,
            "deck_id": self.deck_id,
        }

    @classmethod
    def from_json(cls, json, deck_id):
        return cls(json["front"], json["back"], deck_id)

    @classmethod
    def from_string(cls, front, back, deck_id):
        return cls(front, back, deck_id)
