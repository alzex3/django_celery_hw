from django.db import models


class Advert(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    owner = models.CharField(max_length=30)
    owner_email = models.EmailField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title
