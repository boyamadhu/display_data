from django.db import models

# Create your models here.

class thatre(models.Model):
    t_name=models.CharField(max_length=100,primary_key=True)
    email=models.EmailField(default='madhu@gmail.com')

    def __str__(self):
        return self.t_name
    
class movies(models.Model):
    t_name=models.ForeignKey(thatre,on_delete=models.CASCADE)
    movie_name=models.CharField(max_length=100,)
    movie_release_data=models.DateField()
   

    def __str__(self):
        return self.movie_name

class movie_details(models.Model):
    movie_name=models.ForeignKey(movies,on_delete=models.CASCADE)
    director=models.CharField(max_length=100,)
    hero=models.CharField(max_length=100,)
    heroine=models.CharField(max_length=100,)

    def __str__(self):
        return self.director
    
