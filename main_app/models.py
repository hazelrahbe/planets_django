from django.db import models

class Planet(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_planet = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Info(models.Model):

    namesake = models.CharField(max_length=150)
    years = models.IntegerField(default=0)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name="moons")

    def __str__(self):
        return self.namesake
