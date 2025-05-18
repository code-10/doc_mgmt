from django.urls import path
from .views import CurrentUserView, RegisterView, LoginView, LogoutView, UserDetailAPIView, UserListAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('current_user/', CurrentUserView.as_view(), name='current_user'),

    path('user_list/', UserListAPIView.as_view()),
    path('<int:pk>/', UserDetailAPIView.as_view()),
]
