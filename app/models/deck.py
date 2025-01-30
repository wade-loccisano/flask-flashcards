from app.extensions import db
from .__mixins__ import TimestampMixin

# from sqlalchemy.inspection import inspect
from flask_restful import fields


class Deck(db.Model, TimestampMixin):
    __tablename__ = "Decks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # uuid
    name = db.Column(db.String, nullable=False)
    cards = db.relationship(
        "Card", back_populates="deck", cascade="all, delete", lazy=True
    )

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def __repr__(self):
        return "Deck(name='{}', cards='{}')".format(self.name, self.cards)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "cards": [
                {
                    "id": card.id,
                    "front": card.front,
                    "back": card.back,
                    "deck Id": card.deck_id,
                }
                for card in self.cards
            ],
        }

    @classmethod
    def from_json(cls, json):
        return cls(json["name"], json["cards"])

    @classmethod
    def from_string(cls, str):
        return cls(str, [])
