from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('dish_name',)}
    list_filter = ('status', 'created_on')
    list_display = ('status', 'created_on', 'slug', 'dish_name')
    search_fields = ('dish_name', 'description')
    summernote_fields = ('description', 'ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = ('user_id', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user_id', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)