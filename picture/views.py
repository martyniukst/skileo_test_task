from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render
from .models import Picture

def picture_day(request, id):
    picture = Picture.objects.get(id=id)
    return render(request, 'picture/picture_day.html', {'picture': picture})

def all_pictures(request):
    all_pictures = Picture.objects.all().order_by('-date')
    context = {'all_pictures': all_pictures}
    return render(request, 'picture/pictures.html', context)
