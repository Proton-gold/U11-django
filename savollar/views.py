from unicodedata import category

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from savollar.models import Question


class create(PermissionRequiredMixin,CreateView):
   model=category
   template_name='buss.html'

class QuestionsCreateView(PermissionRequiredMixin,CreateView):
   model=Question




