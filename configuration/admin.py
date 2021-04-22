from django.contrib import admin
from .models import Country, Language, Religion


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country')
    list_filter = ('country', )
    search_fields = ('country', )
    ordering = ('id', 'country')
    list_display_links = ('id', 'country')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'language')
    list_filter = ('language', )
    search_fields = ('language', )
    ordering = ('id', 'language')
    list_display_links = ('id', 'language')


@admin.register(Religion)
class ReligionAdmin(admin.ModelAdmin):
    list_display = ('id', 'religion')
    list_filter = ('religion', )
    search_fields = ('religion', )
    ordering = ('id', 'religion')
    list_display_links = ('id', 'religion')
