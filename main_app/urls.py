from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('list/', views.PlanetList.as_view(), name="planet_list"),
    path('planets/new/', views.PlanetCreate.as_view(), name="planet_create"),
    path('planets/<int:pk>/', views.PlanetDetail.as_view(), name="planet_detail"),
    path('planets/<int:pk>/update',views.PlanetUpdate.as_view(), name="planet_update"),
]