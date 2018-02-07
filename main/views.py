from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
class AboutView(TemplateView):
  template_name  = "about.html"

class HomeView(TemplateView):
  template_name = "home.html"

  def get_object(self):
    object = super().get_object()
    #record the accessed date
    object.last_accessed = timezone.now()
    object.save()
    return object
