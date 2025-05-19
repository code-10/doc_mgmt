import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def admin_user(create_user):
    return create_user(username="adminuser", password="adminpass", role="admin")

@pytest.fixture
def editor_user(create_user):
    return create_user(username="editoruser", password="editorpass", role="editor")

@pytest.fixture
def viewer_user(create_user):
    return create_user(username="vieweruser", password="viewerpass", role="viewer")