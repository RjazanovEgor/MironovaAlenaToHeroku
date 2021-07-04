from django.db import models


# Главная
class MainInform(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    imageURL = models.TextField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Главная'

    def __str__(self):
        return self.name


# О нас
class AboutCompany(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    imageURL = models.TextField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class AboutCompanyPoints(models.Model):
    category = models.ForeignKey(AboutCompany,
                                 related_name='points',
                                 on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('description',)
        verbose_name = 'Пункты'
        verbose_name_plural = 'Пункт'

    def __str__(self):
        return self.description


# Наши услуги
class OurServices(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    description = models.TextField(blank=True)
    # Базовый тариф
    base_description = models.TextField(blank=True)
    base_price = models.DecimalField(max_digits=10,
                                     decimal_places=2)
    # Стандартный тариф
    standard_description = models.TextField(blank=True)
    standard_price = models.DecimalField(max_digits=10,
                                         decimal_places=2)
    # Оптим альный тариф
    optima_description = models.TextField(blank=True)
    optima_price= models.DecimalField(max_digits=10,
                                       decimal_places=2)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Наши услуги'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


# Наши преимущества
class OurAdvantages(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    imageURL = models.TextField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Наши преимущества'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


# Клиенты о нас
class ClientsAboutUs(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True)
    name_client = models.TextField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Клиенты о нас'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


# Статьи
# Модель статей
class Articles(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True)
    article = models.TextField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name


# Модель показываемых статей
class ShowArticle(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True)
    article = models.TextField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.name
