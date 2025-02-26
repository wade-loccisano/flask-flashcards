from app.extensions import db
from app.models.card import Card
from app.models.deck import Deck
from app.utils.mapper import (
    create_hiragana_deck,
    create_katakana_deck,
    create_mixed_deck,
    created_elements_deck,
)


def seed_database(user_id):
    print("Seeding the database...")
    # Decks
    # hiragana_deck = Deck(name="Hiragana Deck", cards=[])
    # katakana_deck = Deck(name="Katakana Deck", cards=[])
    mixed_deck = Deck(name="Kana", user_id=user_id, cards=[])

    elements_deck = Deck(name="Periodic Table of Elements", user_id=user_id, cards=[])

    # db.session.add_all([hiragana_deck, katakana_deck, mixed_deck, elements_deck])
    db.session.add_all([mixed_deck, elements_deck])
    db.session.commit()

    # Create Cards
    # hiragana_cards = create_hiragana_deck(hiragana_deck.id)
    # katakana_cards = create_katakana_deck(katakana_deck.id)
    mixed_cards = create_mixed_deck(mixed_deck.id)

    elements_cards = created_elements_deck(elements_deck.id)

    # db.session.add_all(hiragana_cards)
    # db.session.add_all(katakana_cards)
    db.session.add_all(mixed_cards)
    db.session.add_all(elements_cards)
    db.session.commit()


# if __name__ == "__main__":
#     seed_database()
