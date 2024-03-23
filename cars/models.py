from django.db import models
from rest_framework.authtoken.admin import User


class Cars(models.Model):
    objects = None
    title = models.CharField(max_length=255) # Заголовок
    content = models.TextField(blank=True) # Описание
    time_create = models.DateTimeField(auto_now_add=True) # Создание времени
    time_update = models.DateTimeField(auto_now=True) # Изменение времени
    is_published = models.BooleanField(default=True) # Опубликована ли запись или нет
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True) # ссылка на категорию
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Category(models.Model): # Определяет категорию
    name = models.CharField(max_length=100, db_index=True)


    def __str__(self):
        return self.name
# После нужно создать миграцию