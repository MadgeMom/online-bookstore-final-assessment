import pytest
from app import app, cart, BOOKS

#Global test fixtures that can be accessed and used across multiple test files
@pytest.fixture
def client():
    """Provides a Flask test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client



@pytest.fixture
def filled_cart():
    """Prepopulated cart fixture"""
    cart.clear()
    cart.add_book(BOOKS[0], 2)
    cart.add_book(BOOKS[1], 1)
    yield cart
    cart.clear()

