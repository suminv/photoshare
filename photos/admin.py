from django.contrib import admin
from photos.models import Photo, Category


admin.site.register(Category)
admin.site.register(Photo)

