from django.contrib import admin
from .models import Article
from image_cropping import ImageCroppingMixin
# Register your models here.

class PostAdmin(ImageCroppingMixin,admin.ModelAdmin):
	# list_display = ('title', 'slug', 'author', 'publish', 'status')
	#list_filter = ('status', 'created', 'publish', 'author')
	# search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	#raw_id_fields = ('author',)
	# date_hierarchy = 'publish'
	#ordering = ['status', 'publish']
	exclude = ('cropping','cropping1')


admin.site.register(Article, PostAdmin)
