""" Forms """

from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """ Commenting form """
    class Meta:
        """ Sets model and fields for user form """
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """ Create recipe form """
    class Meta:
        """ Sets model and fields for user form """
        model = Recipe
        fields = ('dish_id', 'suitable_for', 'prep_time', 'cook_time',
                  'description', 'ingredients', 'method',
                  'image', 'status')
        widgets = {
            'method': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }
