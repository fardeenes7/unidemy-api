from django.urls import path, include
from .views import *

urlpatterns = [
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('github/', GithubLogin.as_view(), name='github_login'),
]