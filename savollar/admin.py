from django.contrib import admin
from django.contrib.admin import AdminSite
from accounts.views import register
from savollar.models import Question, Category, Answer

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Answer)
