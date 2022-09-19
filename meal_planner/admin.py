""" Admin """

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """ Settings for the admin recipes panel """

    prepopulated_fields = {'slug': ('dish_id',)}
    list_filter = ('status', 'created_on')
    list_display = ('status', 'created_on', 'slug', 'dish_id')
    search_fields = ('dish_id', 'description')
    summernote_fields = ('description', 'ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Settings for admin comment panel """

    list_display = ('name', 'body', 'recipe', 'created_on')
    list_filter = ('recipe', 'created_on')
    search_fields = ('name', 'body')
