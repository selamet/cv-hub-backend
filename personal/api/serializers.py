from rest_framework import serializers
from personal.models import PersonalDetail, Profile, Education, Experience, Ability, Language, Reference, Hobby, Course, \
    Achievement, Publication


class PersonalDetailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetail
        fields = '__all__'


class CreatePersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetail
        exclude = ['created', 'modified']


class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['created', 'modified']


class CreateExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        exclude = ['created', 'modified']


class CreateAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        exclude = ['created', 'modified']


class CreateLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        exclude = ['created', 'modified']


class CreateReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        exclude = ['created', 'modified']


class CreateHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        exclude = ['created', 'modified']


class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['created', 'modified']


class CreateAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        exclude = ['created', 'modified']


class CreatePublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        exclude = ['created', 'modified']
