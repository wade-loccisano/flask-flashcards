from app import create_app
import pytest


@pytest.fixture(scope="session")
def flask_app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()
