import pytest
from users.serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

def test_register_serializer_valid():
    data = {
        "username": "newuser",
        "email": "new@example.com",
        "password": "strongpass123",
        "role": "editor"
    }
    serializer = RegisterSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert user.username == "newuser"
    assert user.role == "editor"

def test_login_serializer_valid():
    data = {
        "username": "user1",
        "password": "pass123"
    }
    serializer = LoginSerializer(data=data)
    assert serializer.is_valid()

def test_user_serializer():
    user = User.objects.create_user(username="sample", email="sample@example.com", password="pass123", role="viewer")
    serializer = UserSerializer(user)
    assert serializer.data["username"] == "sample"
    assert serializer.data["role"] == "viewer"
