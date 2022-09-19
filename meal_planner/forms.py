""" Forms """

from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """ Commenting form """
    class Meta:
        """ Sets model and fields for user form """
        model = Comment
        fields = ('body',)


class CreateRecipeForm(forms.ModelForm):
    """ Create recipe form """
    class Meta:
        """ Sets model and fields for user form """
        model = Recipe
        fields = ('dish_id', 'suitable_for', 'prep_time', 'cook_time',
                  'description', 'ingredients', 'method',
                  'image', 'status')


class UpdateRecipeForm(forms.ModelForm):
    """ Update recipe form """
    class Meta:
        """ Sets model and fields for user form """
        model = Recipe
        fields = ('dish_id', 'suitable_for', 'prep_time', 'cook_time',
                  'description', 'ingredients', 'method',
                  'image', 'status')
