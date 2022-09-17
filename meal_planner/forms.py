from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('dish_id', 'suitable_for', 'prep_time', 'cook_time',
                  'description', 'ingredients', 'method',
                  'image', 'status')


class UpdateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('dish_id', 'suitable_for', 'prep_time', 'cook_time',
                  'description', 'ingredients', 'method',
                  'image', 'status')
