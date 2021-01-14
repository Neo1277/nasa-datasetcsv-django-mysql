from django.shortcuts import render
from .models import PlanetarySystem
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

class PlanetarySystemsListView(ListView):
    """
    Sub-class the ListView to pass the request to the form.
    """
    model = PlanetarySystem
    # By convention:
    template_name = "planetary_systems/planetary_system_list.html"

# References
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/