from app import cart

def test_checkout_with_items(client, filled_cart): #Successful access to checkout with items in cart
    response = client.get('/checkout')
    assert b'checkout' in response.data.lower()
    assert response.status_code == 200


def test_checkout_empty_cart_redirects(client): #Empty cart handling and redirect
    cart.clear()
    response = client.get('/checkout', follow_redirects=True)
    assert b'your cart is empty' in response.data.lower()



def test_missing_shipping_field(client, filled_cart): #Missing shipping field handling
    data = {
        'name': '',
        'email': 'mom@gmail.com',
        'address': '55 Dunvant Road',
        'city': 'Swansea',
        'zip_code': 'sa27nl',
        'payment_method': 'credit_card',
        'card_number': '1234567890123456',
        'expiry_date': '12/30',
        'cvv': '501',
    }
    response = client.post('/process-checkout', data=data, follow_redirects=True)
    assert b'please fill in the name field' in response.data.lower()
