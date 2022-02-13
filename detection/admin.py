from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Detection


class DetectionAdmin(admin.ModelAdmin):
	list_display = ('id', 'loading_time', 'get_image', 'list_detection')
	readonly_fields = ('get_image', )
	list_display_links = ('id', 'loading_time', 'list_detection')
	search_fields = ('id', 'loading_time')

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image_with_detection_obj.url} width = "160" height = "95"')
	get_image.short_description = 'Изображение'


admin.site.register(Detection, DetectionAdmin)

admin.site.site_title = 'Admin Detection'

admin.site.site_header = 'Admin Detection'

admin.site.site_url = '/input/'