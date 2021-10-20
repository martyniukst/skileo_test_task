from django.db import models, IntegrityError, DataError


class Picture(models.Model):

    name = models.TextField(blank=True, max_length=40)
    description = models.TextField(blank=True)
    url_media = models.TextField(blank=True)
    date = models.DateField(blank=True, unique=True)


    def __str__(self):
        return str(self.to_dict())[1:-1]

    @staticmethod
    def get_by_id(picture_date):
        try:
            picture = Picture.objects.get(id=picture_date)
            return picture
        except Picture.DoesNotExist:
            pass

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'url_media': self.url_media,
            'date': self.date
        }


