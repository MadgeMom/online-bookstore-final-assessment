import pytest
from app import get_book_by_title, BOOKS


def test_get_book_by_title_returns_book_when_found():

    """verifies that get_book_by_title returns the correct Book object when the title provided exists in BOOKS"""
    
    # Arrange (sets up everything needed for the test)
    title = BOOKS[0].title  # Takes the first book in the dictionary list of titles to use a known title from the BOOKS list

    # Act (performs the action to test, i.e. calls the function being tested)
    book = get_book_by_title(title)

    # Assert (will check the outcome is as expected)
    assert book is not None
    assert book.title == title

def test_get_book_by_title_returns_none_when_not_found():

    """verifies that get_book_by_title returns None when the title provided does not exist in BOOKS"""
    
    # Arrange
    title = "This Title Does Not Exist"

    # Act
    book = get_book_by_title(title)

    # Assert
    assert book is None 