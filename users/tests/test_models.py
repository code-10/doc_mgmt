from django.contrib.auth import get_user_model

User = get_user_model()

def test_create_user():
    user = User.objects.create_user(username="testuser", email="test@example.com", password="password123", role="editor")
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.role == "editor"
    assert user.check_password("password123")
