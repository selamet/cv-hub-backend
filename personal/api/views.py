from django.contrib.auth.models import User
from personal.models import *
from rest_framework.generics import CreateAPIView, ListAPIView
from personal.models import PersonalDetail
from personal.api.serializers import CreatePersonalDetailSerializer, PersonalDetailListSerializer, \
    CreateProfileSerializer, CreateExperienceSerializer, CreateAbilitySerializer, CreateLanguageSerializer, \
    CreateReferenceSerializer, CreateHobbySerializer, CreateAchievementSerializer, CreateCourseSerializer, \
    CreatePublicationSerializer, CreateEducationSerializer


class PersonalDetailListAPIView(ListAPIView):
    queryset = PersonalDetail.objects.all()
    serializer_class = PersonalDetailListSerializer


class PersonalDetailCreateAPIView(CreateAPIView):
    queryset = PersonalDetail.objects.all()
    serializer_class = CreatePersonalDetailSerializer


class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = CreateProfileSerializer


class ProfileCreateAPIView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = CreateProfileSerializer


class EducationListAPIView(ListAPIView):
    queryset = Education.objects.all()
    serializer_class = CreateEducationSerializer


class EducationCreateAPIView(CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = CreateEducationSerializer


class ExperienceListAPIView(ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = CreateExperienceSerializer


class ExperienceCreateAPIView(CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = CreateExperienceSerializer


class AbilityListAPIView(ListAPIView):
    queryset = Ability.objects.all()
    serializer_class = CreateAbilitySerializer


class AbilityCreateAPIView(CreateAPIView):
    queryset = Ability.objects.all()
    serializer_class = CreateAbilitySerializer


class LanguageListAPIView(ListAPIView):
    queryset = Language.objects.all()
    serializer_class = CreateLanguageSerializer


class LanguageCreateAPIView(CreateAPIView):
    queryset = Language.objects.all()
    serializer_class = CreateLanguageSerializer


class ReferenceListAPIView(ListAPIView):
    queryset = Reference.objects.all()
    serializer_class = CreateReferenceSerializer


class ReferenceCreateAPIView(CreateAPIView):
    queryset = Reference.objects.all()
    serializer_class = CreateReferenceSerializer


class HobbyListAPIView(ListAPIView):
    queryset = Hobby.objects.all()
    serializer_class = CreateHobbySerializer


class HobbyCreateAPIView(CreateAPIView):
    queryset = Hobby.objects.all()
    serializer_class = CreateHobbySerializer


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CreateCourseSerializer


class CourseCreateAPIView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CreateCourseSerializer


class AchievementListAPIView(ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = CreateAchievementSerializer


class AchievementCreateAPIView(CreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = CreateAchievementSerializer


class PublicationListAPIView(ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = CreatePublicationSerializer


class PublicationCreateAPIView(CreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = CreatePublicationSerializer
