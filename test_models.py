import pytest
from models import Cart, Book, CartItem

def test_book_initialization():

    """verifies a book object is correctly initialised, i.e. with title, category, price and image"""
    
    book = Book("Test Title", "Fiction", 19.99, "image.jpg")
    assert book.title == "Test Title"
    assert book.category == "Fiction"
    assert book.price == 19.99
    assert book.image == "image.jpg"

def test_cartitem_initialization_and_total_price():

    """verifies a Cartitem is correctly initialised, i.e. with book and quantity.  
    Will verify the get_total_price() method works as expected, i.e. price x quantity"""
    
    book = Book("Book1", "Category", 10.0, "img.jpg")
    item = CartItem(book, 3)
    assert item.book == book
    assert item.quantity == 3
    assert item.get_total_price() == 30.0

def test_cart_initialization():

    """verifies a new Cart begins empty with no items"""

    cart = Cart()
    assert cart.items == {}
    assert cart.is_empty()

def test_cart_add_book_new_and_existing():

    """verifies a new book can be added to the cart, i.e. should appear in items with correct quantity, 
    and the same book can be added to the cart again, i.e. the quantity of that book should increased if added again"""
       
    cart = Cart()
    book = Book("Book1", "Cat", 5.0, "img.jpg")
    cart.add_book(book, 2)
    assert "Book1" in cart.items
    assert cart.items["Book1"].quantity == 2

    # Add same book again
    cart.add_book(book, 3)
    assert cart.items["Book1"].quantity == 5

def test_cart_remove_book():
    """verifies a book can be removed from the cart by title, and removing a non-existing book does nothing"""

    cart = Cart()
    book = Book("Book1", "Cat", 5.0, "img.jpg")
    cart.add_book(book, 1)
    cart.remove_book("Book1")
    assert "Book1" not in cart.items

    # Removing non-existing book does nothing
    cart.remove_book("Nonexistent")
    assert "Nonexistent" not in cart.items

def test_cart_update_quantity_positive_and_zero():
    """verifies that updating the book quantity to a positive number changes the quantity accordingly
    and that updating to zero removes the book from the cart"""
    
    cart = Cart()
    book = Book("Book1", "Cat", 5.0, "img.jpg")
    cart.add_book(book, 2)
    cart.update_quantity("Book1", 10)
    assert cart.items["Book1"].quantity == 10

    # Update to zero removes the book
    cart.update_quantity("Book1", 0)
    assert "Book1" not in cart.items

def test_cart_update_quantity_negative_removes():

    """verifies that updating the book quantity to a negative number removes the book from the cart"""

    cart = Cart()
    book = Book("Book1", "Cat", 5.0, "img.jpg")
    cart.add_book(book, 2)
    cart.update_quantity("Book1", -5)
    assert "Book1" not in cart.items

def test_cart_get_total_price_and_items():
    """verifies the get_total_price() method returns the correct total sum of all items in the cart
    and that get_total_items() method returns the correct total quantity of books in the cart"""

    cart = Cart()
    book1 = Book("Book1", "Cat", 5.0, "img.jpg")
    book2 = Book("Book2", "Cat", 7.5, "img2.jpg")
    cart.add_book(book1, 2)  # 10.0
    cart.add_book(book2, 3)  # 22.5
    assert cart.get_total_price() == 32.5
    assert cart.get_total_items() == 5

def test_cart_clear():

    """verifies the clear() method removes all items from the cart and the cart is then empty"""

    cart = Cart()
    book = Book("Book1", "Cat", 5.0, "img.jpg")
    cart.add_book(book, 1)
    cart.clear()
    assert cart.items == {}
    assert cart.is_empty()

def test_cart_get_items():

    """verifies the get_items() method returns a list of all CartItem objects currently in the cart"""

    #adds books to cart and verifies get_items() returns correct list of CartItem objects
    cart = Cart()
    book1 = Book("Book1", "Cat", 5.0, "img.jpg")
    book2 = Book("Book2", "Cat", 7.5, "img2.jpg")
    cart.add_book(book1, 1)
    cart.add_book(book2, 2)
    items = cart.get_items()
    assert len(items) == 2
    titles = {item.book.title for item in items}
    assert titles == {"Book1", "Book2"}

def test_cart_is_empty_true_and_false():

    """verifies the is_empty() method returns True for an empty cart and False when there are items in the cart"""

    #verifies a new cart if empty, then adds book and verifies cart is no longer empty
    cart = Cart()
    assert cart.is_empty()
    book = Book("Book1", "Cat", 5.0, "img.jpg")
    cart.add_book(book, 1)
    assert not cart.is_empty()
