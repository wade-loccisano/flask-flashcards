# Flask Flashcards

A simple flashcard utility created with Flask in Python that uses a PostgreSQL database.

[See it Live hosted on Render](https://flashcards-lite.onrender.com "Flashcards Lite")

## How to Run

### Local Requirements

- Python 3
- PostgreSQL
- Docker (optional if preferred)

### Install python dependencies

1. Create a virtual environment:

    ```
    py -m venv .venv
    ```

2. Activate your virtual environment:

    ```
    source .venv/Scripts/activate
    ```

3. Using pip:

    ```
    pip install -r requirements.txt
    ```

### Configure environment variables

Create an `.env` file using `_.env` as an example.

```
SECRET_KEY=
RECAPTCHA_PUBLIC_KEY=
RECAPTCHA_PRIVATE_KEY=
DATABASE_URL=
```

### Run migrations

1. Apply the migrations in the Migrations folder:

    ```
    flask db upgrade
    ```

### Run the app

```
python app.py
```

The server will be running on `http://127.0.0.1:5000/`

## TODO

- [x] Seed demo decks and cards
- [x] Auth
- [x] Deploy Build
- [ ] Readme Migrations Section
- [ ] Docker Support
- [ ] Unit tests
- [ ] Logging
- [ ] CI/CD