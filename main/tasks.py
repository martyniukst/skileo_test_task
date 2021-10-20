from celery import shared_task
from picture.models import Picture
from datetime import date, timedelta
import requests
import urllib.request

@shared_task
def get_new_picture_of_a_day():
    all_pictures = [item.date.strftime("%Y-%m-%d") for item in Picture.objects.all()]
    url = 'https://api.nasa.gov/planetary/apod?api_key=hAXazJhJmSYmcMdMwIXbnjVwHRbwNSjLkQ46bhuK'
    r = requests.get(url)
    item = r.json()
    if item['date'] not in all_pictures:
        p = Picture(name=item['title'], description=item['explanation'], url_media=item['url'], date=item['date'])
        p.save()
        if item['url'][-4:] =='.jpg':
            urllib.request.urlretrieve(item['url'], 'picture/images/' + str(item['url']).split('/')[-1])

def one_time_startup_function():
    start_date = date.today() - timedelta(days=14)
    all_pictures = [item.date.strftime("%Y-%m-%d") for item in Picture.objects.all()]
    url = 'https://api.nasa.gov/planetary/apod?api_key=hAXazJhJmSYmcMdMwIXbnjVwHRbwNSjLkQ46bhuK&start_date='+str(start_date)
    r = requests.get(url)
    list = r.json()
    for item in list:
        if item['date'] not in all_pictures:
            p = Picture(name=item['title'], description=item['explanation'], url_media=item['url'], date=item['date'])
            p.save()
            if item['url'][-4:] =='.jpg':
                urllib.request.urlretrieve(item['url'], 'picture/images/' + str(item['url']).split('/')[-1])