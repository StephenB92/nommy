""" URLs """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('createrecipe/', views.RecipeCreate.as_view(), name='create_recipe'),
    path('myrecipes/', views.MyRecipes.as_view(), name='my_recipes'),
    path('likedrecipes/', views.LikedRecipes.as_view(), name='liked_recipes'),
    path('<slug:slug>/updaterecipe/', views.RecipeUpdate.as_view(),
         name='update_recipe'),
    path('<slug:slug>/deleterecipe/', views.RecipeDelete.as_view(),
         name='delete_recipe'),
    path('likes/<slug:slug>/', views.RecipeLikes.as_view(),
         name='recipe_likes'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]
