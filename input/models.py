from django.db import models

# Create your models here.

class Input(models.Model):
    loading_time = models.DateTimeField(auto_now_add = True, verbose_name = 'Время загрузки')
    image = models.ImageField(upload_to = 'images/%Y/%m/%d/', verbose_name = 'Изображение')
    def __str__(self):
    	return str(self.pk)
    class Meta:
    	verbose_name = 'Запись'
    	verbose_name_plural = 'Записи'
    	ordering = ['-loading_time']