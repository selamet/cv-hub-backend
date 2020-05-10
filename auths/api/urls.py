from django.urls import path, include

from auths.api.views import CreateUserView

app_name = 'auths'

urlpatterns = [
    path('register', CreateUserView.as_view(), name='register'),
]
