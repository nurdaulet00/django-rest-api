from django.contrib import admin

from .models import Cars
# В администрирование джанго появляется таблица
admin.site.register(Cars)