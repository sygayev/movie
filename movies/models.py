from django.db import models
from datetime import date

class Category(models.Model):
    #Категории
    name = models.CharField("Категории", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
class Actor(models.Model):
    "Актеры и режиссеры"
    name = models.CharField("Имя" , max_length=100)
    age = models.PositiveSmallIntegerField("Возвраст", default= 0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"
        
        
class Genre(models.Model):
    "Жанры"
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        

class Model(models.Model):
    "Фильмы"
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movie/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2023)
    country =  models.CharField("Страна", max_length= 30)
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actor = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Жанры")
    world_premiere = models.DateField("Премьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField("Сборы в США", default= 0, help_text= "указать сумму в долларах")
    fees_in_world = models.PositiveIntegerField("Сборы в мире", default= 0, help_text= "указать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null = True)
    
    