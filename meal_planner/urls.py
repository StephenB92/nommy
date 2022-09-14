from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('createrecipe', views.RecipeCreate.as_view(), name='create_recipe'),
    path('likes/<slug:slug>/', views.RecipeLikes.as_view(),
         name='recipe_likes'),
]
