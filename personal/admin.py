from django.contrib import admin

from personal.models import PersonalDetail, Profile, Education, Ability, Language, Course, Experience, Hobby, Reference, \
    Achievement, Publication

# Register your models here.


admin.site.register(PersonalDetail)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Ability)
admin.site.register(Language)
admin.site.register(Course)
admin.site.register(Experience)
admin.site.register(Hobby)
admin.site.register(Reference)
admin.site.register(Achievement)
admin.site.register(Publication)
