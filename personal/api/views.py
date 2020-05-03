from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView
from personal.models import PersonalDetail
from personal.api.serializers import CreatePersonalDetailSerializer, PersonalDetailListSerializer


class PersonalDetailListAPIView(ListAPIView):
    queryset = PersonalDetail.objects.all()
    serializer_class = PersonalDetailListSerializer


class PersonalDetailCreateAPIView(CreateAPIView):
    queryset = PersonalDetail.objects.all()
    serializer_class = CreatePersonalDetailSerializer

    def save(self):
        pass
