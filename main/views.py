from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from picture.models import Picture
from datetime import date


def picture_of_a_day(request):
    # today = date.today()
    # picture = Picture.objects.all(date=today)
    all_pictures = Picture.objects.all().order_by('-date')
    paginator = Paginator(all_pictures, 1)
    page = request.GET.get('page')
    try:
        all_pictures = paginator.page(page)
    except PageNotAnInteger:
        all_pictures = paginator.page(1)
    except EmptyPage:
        all_pictures = paginator.page(paginator.num_pages)
    context = {'all_pictures': all_pictures}
    return render(request, 'main/index.html', context)