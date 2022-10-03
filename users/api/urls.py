from django.urls import path, include
from users.api.views import RegisterView


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
]