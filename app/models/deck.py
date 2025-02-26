from app.extensions import db
from .__mixins__ import TimestampMixin


class Deck(db.Model, TimestampMixin):
    __tablename__ = "Decks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(
        db.String(36), db.ForeignKey("Users.id", ondelete="CASCADE"), nullable=False
    )
    user = db.relationship("User", back_populates="decks")
    cards = db.relationship(
        "Card", back_populates="deck", cascade="all, delete-orphan", lazy=True
    )

    def __init__(self, name, user_id, cards):
        self.name = name
        self.user_id = user_id
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
                    "deckId": card.deck_id,
                }
                for card in self.cards
            ],
        }

    @classmethod
    def from_json(cls, json):
        return cls(json["name"], json["cards"])

    @classmethod
    def from_string(cls, name, user_id, cards=[]):
        return cls(name, user_id, cards)
