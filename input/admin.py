from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Input


class InputAdmin(admin.ModelAdmin):
	list_display = ('id', 'loading_time', 'get_image')
	readonly_fields = ('get_image', )
	list_display_links = ('id', 'loading_time')
	search_fields = ('id', 'loading_time')

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.image.url} width = "160" height = "95"')
	get_image.short_description = 'Изображение'


admin.site.register(Input, InputAdmin)

admin.site.site_title = 'Admin Detection'

admin.site.site_header = 'Admin Detection'
admin.site.site_url = '/input/'