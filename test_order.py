from unittest.mock import patch
from models import Order, Book, CartItem

def test_order_confirmation_valid(client):
    # Create mock order with realistic payment_info
    payment_info = {"method": "credit_card"}
    order = Order("ORDER123", "test@example.com", [], {}, payment_info, 99.99)
    from app import orders
    orders["ORDER123"] = order

    response = client.get('/order-confirmation/ORDER123')
    assert response.status_code == 200
    assert b'order' in response.data.lower()




def test_order_confirmation_invalid_id(client):
    response = client.get('/order-confirmation/INVALID', follow_redirects=True)
    assert b'order not found' in response.data.lower()


@patch('models.EmailService.send_order_confirmation')
def test_email_service_called(mock_send, client, filled_cart):
    data = {
        'name': 'Test User',
        'email': 'test@example.com',
        'address': '123 Elm St',
        'city': 'Metro City',
        'zip_code': '54321',
        'payment_method': 'credit_card',
        'card_number': '9999888877776666',
        'expiry_date': '12/30',
        'cvv': '321'
    }
    client.post('/process-checkout', data=data, follow_redirects=True)
    mock_send.assert_called_once()
