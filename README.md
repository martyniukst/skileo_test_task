python3 manage.py runserver

#for autimatic update

celery -A skileo worker -l info

celery -A skileo beat -l info
