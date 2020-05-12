from django.urls import path, include

from auths.api.views import CreateUserView, UpdatePassword

app_name = 'auths'

urlpatterns = [
    path('register', CreateUserView.as_view(), name='register'),
    path('change-password', UpdatePassword.as_view(), name='change-password'),

]
