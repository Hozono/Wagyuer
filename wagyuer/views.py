from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import HttpResponse
 

class Index(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foo"] = "bar"
        return context