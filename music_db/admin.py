from django.contrib import admin

# Register your models here.
from music_db.models import Category, Music

admin.site.register(Category)
admin.site.register(Music)

