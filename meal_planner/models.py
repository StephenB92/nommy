""" Models """

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    """ Model for Recipes """
    dish_id = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='recipes')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    suitable_for = models.CharField(max_length=80)
    prep_time = models.CharField(max_length=20, default=0)
    cook_time = models.CharField(max_length=20, default=0)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes',
                                   default=None, blank=True)

    class Meta:
        """ Ensures recipes are listed in date order """
        ordering = ['-created_on']

    # Credit to Stack Overflow for the "save" method below.

    def save(self, *args, **kwargs):
        """ Function ensuring a user created recipe generates a new slug """
        self.slug = slugify(self.dish_id)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        """ Returns the dish_id """
        return f"{self.dish_id}"

    def get_absolute_url(self):
        """ Obtains recipe_detail page after user edits """
        return reverse('recipe_detail', kwargs={'slug': self.slug})

    def get_delete_url(self):
        """ Obtains my_recipes page after user deletes """
        return reverse('my_recipes', kwargs={'slug': self.slug})

    # Credit to Stack Overflow for the "get_STATUS_display" method below.

    def get_STATUS_display(self):
        """
        Obtains recipe draft/published status
        for user on my_recipes page
        """
        return self.status

    def number_of_likes(self):
        """ Obtains the number of likes on a recipe """
        return self.likes.count()


class Comment(models.Model):
    """ Model for Comments """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='comments')
    name = models.CharField(max_length=80, null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Ensures comments are listed in date order """
        ordering = ['created_on']

    def __str__(self):
        """ Returns the user comment """
        return f"Comment {self.body} by {self.name}"
