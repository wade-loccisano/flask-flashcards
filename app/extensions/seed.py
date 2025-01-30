from app.extensions import db
from app.models.card import Card
from app.models.deck import Deck


def seed_database():
    print("Seeding the database...")
    # Decks
    hiragana_deck = Deck(name="Hiragana Deck", cards=[])
    katakana_deck = Deck(name="Katakana Deck", cards=[])
    mixed_deck = Deck(name="Hiragana/Katakana Deck", cards=[])

    db.session.add_all([hiragana_deck])
    db.session.commit()

    # Create Cards
    card_h_1 = Card(front="あ", back="a", deck_id=hiragana_deck.id)
    card_h_2 = Card(front="い", back="i", deck_id=hiragana_deck.id)
    card_h_3 = Card(front="う", back="u", deck_id=hiragana_deck.id)
    card_h_4 = Card(front="え", back="e", deck_id=hiragana_deck.id)
    card_h_5 = Card(front="お", back="o", deck_id=hiragana_deck.id)

    db.session.add_all(
        [
            card_h_1,
            card_h_2,
            card_h_3,
            card_h_4,
            card_h_5,
        ]
    )
    db.session.commit()


# if __name__ == "__main__":
#     seed_database()


def seed_db(app):
    """Seed the database with initial data."""
    with app.app_context():
        db.drop_all()  # Optional: Clears existing data
        db.create_all()  # Ensures tables exist

        # # Add seed data
        # cards = [
        #     Card(front="What is Flask?", back="A Python web framework"),
        #     Card(front="What is Jinja2?", back="A templating engine for Flask"),
        #     Card(front="What is SQLAlchemy?", back="A Python ORM for databases"),
        # ]
        # Decks
        hiragana_deck = Deck(name="Hiragana Deck", cards=[])
        katakana_deck = Deck(name="Katakana Deck", cards=[])
        mixed_deck = Deck(name="Hiragana/Katakana Deck", cards=[])

        # Create Cards
        card_h_1 = Card(front="あ", back="a", deck_id=hiragana_deck.id)

        db.session.bulk_save_objects([hiragana_deck, card_h_1])
        db.session.commit()
        print("Database seeded successfully!")
