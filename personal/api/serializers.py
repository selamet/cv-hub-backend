from rest_framework import serializers
from personal.models import PersonalDetail


class PersonalDetailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetail
        fields = '__all__'


class CreatePersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetail
        exclude = ['created', 'modified']
