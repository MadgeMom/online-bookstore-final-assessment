from models import PaymentGateway

def test_payment_success(): #checks successful payment processing
    payment_info = {
        'payment_method': 'credit_card',
        'card_number': '1234123412341234',
        'expiry_date': '12/27',
        'cvv': '123'
    }
    result = PaymentGateway.process_payment(payment_info) #checks for successful payment
    assert result['success'] is True
    assert 'TXN' in result['transaction_id']


def test_payment_failure_due_to_invalid_card(): #checks payment failure with invalid card number
    payment_info = {
        'payment_method': 'credit_card',
        'card_number': '1111',
        'expiry_date': '12/28',
        'cvv': '222'
    }
    result = PaymentGateway.process_payment(payment_info)
    assert result['success'] is False
    assert 'Invalid card number' in result['message']

#many more tests could be added here to cover edge cases and different payment methods, expiry dates, etc.