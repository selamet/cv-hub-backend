from django.urls import path, include
from personal.api.views import *

app_name = 'personal'

urlpatterns = [
    path('personal-detail-list', PersonalDetailListAPIView.as_view(), name='personal-detail-list'),
    path('personal-create', PersonalDetailCreateAPIView.as_view(), name='personal-create'),

    path('profile-create', ProfileCreateAPIView.as_view(), name='profile-create'),
    path('education-create', EducationCreateAPIView.as_view(), name='education-create'),
    path('experience-create', ExperienceCreateAPIView.as_view(), name='experience-create'),
    path('ability-create', AbilityCreateAPIView.as_view(), name='ability-create'),
    path('language-create', LanguageCreateAPIView.as_view(), name='language-create'),
    path('reference-create', ReferenceCreateAPIView.as_view(), name='reference-create'),
    path('hobby-create', HobbyCreateAPIView.as_view(), name='hobby-create'),
    path('course-create', CourseCreateAPIView.as_view(), name='course-create'),
    path('achievement-create', AchievementCreateAPIView.as_view(), name='achievement-create'),
    path('publication-create', PublicationCreateAPIView.as_view(), name='publication-create'),
    path('personal-history-list', PersonalHistoryListAPIView.as_view(), name='personal-history-list'),
]
