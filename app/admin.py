from django.contrib import admin
from .models import Articles, ShowArticle, AboutCompany, OurAdvantages, \
    OurServices, ClientsAboutUs, MainInform, AboutCompanyPoints


@admin.register(MainInform)
class MainInformAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'imageURL',
                    'description']
    list_display_links = None
    list_filter = ['name']
    list_editable = ['name', 'slug', 'imageURL',
                     'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'imageURL',
                    'description']
    list_display_links = None
    list_filter = ['name']
    list_editable = ['name', 'slug', 'imageURL',
                     'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(AboutCompanyPoints)
class AboutCompanyPoints(admin.ModelAdmin):
    list_display = ['description']
    list_display_links = None
    list_editable = ['description']


@admin.register(OurServices)
class OurServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description',
                    'base_description', 'base_price',
                    'standard_description', 'standard_price',
                    'optima_description', 'optima_price']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(OurAdvantages)
class OurAdvantagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'imageURL',
                    'description']
    list_display_links = None
    list_filter = ['name']
    list_editable = ['name', 'slug', 'imageURL',
                     'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'article',
                    'description', 'date']
    list_display_links = None
    list_filter = ['name', 'date']
    list_editable = ['name', 'slug', 'article',
                     'description', 'date']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ShowArticle)
class ShowArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'article',
                    'description', 'date']
    list_display_links = None
    list_filter = ['name', 'date']
    list_editable = ['name', 'slug', 'article',
                     'description', 'date']
    prepopulated_fields = {'slug': ('name',)}
