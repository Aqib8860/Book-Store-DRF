from django.urls import path
from user.views import RegisterView, UserProfileView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('user/profile/', UserProfileView.as_view(), name='user_profile'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain'),
    path('', jwt_views.TokenObtainPairView.as_view(), name='token_obtain'),
]