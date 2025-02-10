from app.utils.exceptions import BadRequestException


def validate_create_deck(body: dict) -> None:
    deck_fields = ["name"]
    for field in deck_fields:
        if field not in body:
            raise BadRequestException(f"Missing {field} parameter.")

    if not isinstance(body["name"], str):
        raise BadRequestException("Invalid JSON.")


def validate_edit_deck(body: dict) -> None:
    deck_fields = ["name"]
    for field in deck_fields:
        if field not in body:
            raise BadRequestException(f"Missing {field} parameter.")

    if not isinstance(body["name"], str):
        raise BadRequestException("Invalid JSON.")
