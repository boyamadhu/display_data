from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import *

def display_movie_details(request):
    tname=input('enter theatre name : ')
    TO=thatre.objects.get_or_create(t_name=tname)[0]
    TO.save()

    
    mov_name=input('enter movie name : ')
    mov_release=input('enter movie release date : ')
    MO=movies.objects.get_or_create(t_name=TO,movie_name=mov_name,movie_release_data=mov_release)[0]
    MO.save()

    
    direc=input('enter director name : ')
    hero_name=input('enter hero name : ')
    heroine_name=input('enter heroine name : ')
    MO1=movie_details.objects.get_or_create(movie_name=MO,director=direc,hero=hero_name,heroine=heroine_name)[0]
    MO1.save()

    return HttpResponse('inserted successfully')


def display_movie(request):
    TO=movie_details.objects.all()
    d={'display' : TO}
    return render(request,'first.html',d)

    
