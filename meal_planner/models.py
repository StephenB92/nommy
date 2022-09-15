from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
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
        ordering = ['-created_on']

    def __str__(self):
        return self.dish_id

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.slug})

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
