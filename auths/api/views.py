from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from auths.api.permissions import NotAuthenticated
from rest_framework.generics import CreateAPIView

from auths.api.serializers import RegisterSerializer
from auths.api.throttles import RegisterThrottle


class CreateUserView(CreateAPIView):
    throttle_classes = [RegisterThrottle]
    model = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (NotAuthenticated,)
