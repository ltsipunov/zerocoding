from django.db import models

class Film(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=255)
    review = models.TextField('Отзыв')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'