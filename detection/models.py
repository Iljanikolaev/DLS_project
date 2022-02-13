from django.db import models

# Create your models here.

class Detection(models.Model):
    loading_time = models.DateTimeField(auto_now_add = True, verbose_name = 'Время загрузки')
    image_with_detection_obj = models.ImageField(upload_to = 'detection_img/%Y/%m/%d/', verbose_name = 'Изображение с распознанными объектами')
    list_detection = models.TextField(blank=True, verbose_name = 'Список распознанных объектов')
    def __str__(self):
    	return str(self.pk)
    class Meta:
    	verbose_name = 'Запись'
    	verbose_name_plural = 'Записи'
    	ordering = ['-loading_time']