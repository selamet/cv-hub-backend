from django.urls import path, include
from personal.api.views import PersonalDetailCreateAPIView, PersonalDetailListAPIView

app_name = 'personal'

urlpatterns = [
    path('personal-detail-list', PersonalDetailListAPIView.as_view(), name='personal-detail-list'),
    path('personal-create', PersonalDetailCreateAPIView.as_view(), name='personal-create'),
]
