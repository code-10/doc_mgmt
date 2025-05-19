import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@pytest.mark.django_db
def test_register_view(api_client):
    data = {
        "username": "reguser",
        "email": "reg@example.com",
        "password": "pass12345",
        "role": "editor"
    }
    response = api_client.post("/api/users/register/", data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username="reguser").exists()

@pytest.mark.django_db
def test_login_view(api_client, create_user):
    create_user(username="loginuser", password="secret123")
    response = api_client.post("/api/users/login/", {
        "username": "loginuser",
        "password": "secret123"
    })
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_current_user_view(api_client, admin_user):
    refresh = RefreshToken.for_user(admin_user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    response = api_client.get("/api/users/me/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["username"] == "adminuser"

@pytest.mark.django_db
def test_user_list(api_client, admin_user):
    refresh = RefreshToken.for_user(admin_user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    response = api_client.get("/api/users/")
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_user_detail(api_client, admin_user):
    user = User.objects.create_user(username="someone", password="pass123", email="some@example.com", role="viewer")
    refresh = RefreshToken.for_user(admin_user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    response = api_client.get(f"/api/users/{user.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["username"] == "someone"

@pytest.mark.django_db
def test_user_delete(api_client, admin_user):
    user = User.objects.create_user(username="todelete", password="pass", role="viewer")
    refresh = RefreshToken.for_user(admin_user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    response = api_client.delete(f"/api/users/{user.id}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not User.objects.filter(id=user.id).exists()
