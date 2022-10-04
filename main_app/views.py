from re import template
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Planet
# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(View):

    # Here we are adding a method that will be run when we are dealing with a GET request
    def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("Planets Home")

#...
class About(View):

    def get(self, request):
        return HttpResponse("Planets About")

class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class PlanetList(View):
     def get(self, request):
        return HttpResponse("Planets List")

class PlanetList(TemplateView):
    template_name = "planet_list.html"
 #adds artist class for mock database data
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["planets"] = Planet.objects.all() # this is where we add the key into our context object for the view to use
        return context
