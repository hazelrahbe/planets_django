from re import template
from unicodedata import name
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Planet, Info, Surface
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
# class Home(View):

#     # Here we are adding a method that will be run when we are dealing with a GET request
#     def get(self, request):
#         # Here we are returning a generic response
#         # This is similar to response.send() in express
#         return HttpResponse("Planets Home")

#...
class About(View):

    def get(self, request):
        return HttpResponse("Planets About")

class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["surfaces"] = Surface.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class PlanetList(View):
     def get(self, request):
        return HttpResponse("Planets List")

class PlanetList(TemplateView):
    template_name = "planet_list.html"
 #adds planet class for mock database data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["planets"] = Planet.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context["planets"] = Planet.objects.all()# this is where we add the key into our context object for the view to use
            context["header"] = "WellKnown Planets"
        return context

class PlanetCreate(CreateView):
    model = Planet
    fields = ['name', 'img', 'bio', 'verified_planet']
    template_name = "planet_create.html"
    def get_success_url(self):
        return reverse('planet_detail', kwargs={'pk': self.object.pk})

class PlanetDetail(DetailView):
    model = Planet
    template_name = "planet_detail.html"

class PlanetUpdate(UpdateView):
    model = Planet
    fields = ['name', 'img', 'bio', 'verified_planet']
    template_name = "planet_update.html"
    def get_success_url(self):
        return reverse('planet_detail', kwargs={'pk': self.object.pk})

class PlanetDelete(DeleteView):
    model = Planet
    template_name = "planet_delete.html"
    success_url = "/list/"

