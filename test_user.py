from app import users

def test_register_new_user(client): # checks successful user registration
    data = {
        'email': 'newuser@gmail.com',
        'password': 'safe123',
        'name': 'New User',
        'address': '123 Broadway'
    }
    response = client.post('/register', data=data, follow_redirects=True)
    assert b'account created successfully' in response.data.lower()
    assert 'newuser@gmail.com' in users


def test_register_duplicate_email(client): #checks duplicate email registration handling
    data = {
        'email': 'demo@bookstore.com',
        'password': 'demo123',
        'name': 'Demo Again'
    }
    response = client.post('/register', data=data, follow_redirects=True)
    assert b'already exists' in response.data.lower()


def test_login_success_and_fail(client): #checks login with valid and invalid credentials
    # Valid credentials
    response = client.post('/login', data={'email': 'demo@bookstore.com', 'password': 'demo123'}, follow_redirects=True)
    assert b'logged in successfully' in response.data.lower()

    # Invalid credentials
    response = client.post('/login', data={'email': 'demo@bookstore.com', 'password': 'wrong'}, follow_redirects=True)
    assert b'invalid email or password' in response.data.lower()


def test_update_profile(client): #checks profile update functionality
    # Simulate login 
    with client.session_transaction() as sess:
        sess['user_email'] = 'demo@bookstore.com'
# Update profile
    response = client.post('/update-profile', data={'name': 'Updated User', 'new_password': 'newpass'}, follow_redirects=True)
    assert b'password updated successfully' in response.data.lower()
    assert users['demo@bookstore.com'].name == 'Updated User'


def test_logout(client):
    with client.session_transaction() as sess:
        sess['user_email'] = 'demo@bookstore.com'

    response = client.get('/logout', follow_redirects=True)
    assert b'logged out successfully' in response.data.lower()
    with client.session_transaction() as sess:
        assert 'user_email' not in sess
