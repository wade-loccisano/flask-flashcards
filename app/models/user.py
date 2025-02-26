import uuid
from datetime import datetime
from app.extensions import db
from flask_login import UserMixin
from .__mixins__ import TimestampMixin


class User(db.Model, UserMixin, TimestampMixin):
    __tablename__ = "Users"

    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        unique=True,
        nullable=False,
    )
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.now())

    decks = db.relationship(
        "Deck", back_populates="user", cascade="all, delete-orphan", lazy=True
    )

    def __init__(self, username, password_hash):
        self.username = username
        self.password_hash = password_hash

    def __repr__(self):
        return "User(username='{}')".format(self.username)

    def serialize(self):
        return {"id": self.id, "username": self.username}

    @classmethod
    def from_json(cls, json):
        return cls(json["username"])
