from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='название локации')
    description_short = models.TextField(verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    longitude = models.DecimalField(max_digits=22, decimal_places=16, verbose_name='Долгота')
    latitude = models.DecimalField(max_digits=22, decimal_places=16, verbose_name='Широта')

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    title = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Локация')
    image = models.ImageField(null=True, blank=False, verbose_name='Изображение')
    number = models.IntegerField(default=1, verbose_name='Номер изображения')

    def __str__(self) -> str:
        return f'{self.number} {self.title}'
