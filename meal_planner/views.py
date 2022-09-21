""" Views """

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Recipe
from .forms import CommentForm, RecipeForm


class RecipeList(generic.ListView):
    """
    This view is used to allow the user to view a list of recipes.
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 9


class RecipeDetail(generic.DetailView):
    """
    This view is used to allow users to view  recipes in detail.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        This function obtains recipe data to display to the user.
        """
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        This function allows logged in users to comment on recipes.
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.success(self.request, 'Your comment has been added.')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class RecipeLikes(View):
    """
    This view is used to allow users to see the number of likes
    attached to recipes.
    """
    def post(self, request, slug):
        """
        This function allows users to like or unlike recipes.
        """
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class RecipeCreate(LoginRequiredMixin, SuccessMessageMixin,
                   generic.CreateView):
    """
    This view is used to allow the logged in user to create their own recipes.
    """
    form_class = RecipeForm
    template_name = 'create_recipe.html'
    success_message = "%(calculated_field)s was created successfully"

    def form_valid(self, form):
        """
        This method ensures that the user is set as the creator of the recipe.
        """
        form.instance.creator = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function adds the recipe title into the success message.
        Credit to the Django Documentation.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.dish_id,
        )


class RecipeUpdate(LoginRequiredMixin, SuccessMessageMixin,
                   generic.UpdateView):
    """
    This view is used to allow the logged in user to update their recipes.
    """
    queryset = Recipe.objects.all()
    form_class = RecipeForm
    template_name = 'update_recipe.html'
    success_message = "%(calculated_field)s was updated successfully"

    def form_valid(self, form):
        """
        This method ensures that the user is set as the creator of the recipe.
        """
        form.instance.creator = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        """
        This function adds the recipe title into the success message.
        Credit to the Django Documentation.
        """
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.dish_id,
        )


class RecipeDelete(LoginRequiredMixin, generic.DeleteView):
    """
    This view is used to allow the logged in user to delete their recipes.
    """
    queryset = Recipe.objects.all()
    template_name = 'delete_recipe.html'
    success_message = "Recipe was deleted successfully"
    success_url = reverse_lazy('my_recipes')

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display a delete message.
        Credit to Stack Overflow.
        """
        messages.warning(self.request, self.success_message)
        return super(RecipeDelete, self).delete(request, *args, **kwargs)


class MyRecipes(LoginRequiredMixin, generic.ListView):
    """
    This view is used to display a list of recipes created by the logged in
    user.
    """
    model = Recipe
    template_name = 'my_recipes.html'
    paginate_by = 9

    def get_queryset(self):
        """
        Function which filters the my recipes page to those
        created by the user.
        """
        return Recipe.objects.filter(creator=self.request.user)


class LikedRecipes(LoginRequiredMixin, generic.ListView):
    """
    This view is used to display a list of recipes liked by the logged in
    user.
    """
    model = Recipe
    template_name = 'liked_recipes.html'
    paginate_by = 9

    def get_queryset(self):
        """
        Function which filters the my recipes page to those
        liked by the user.
        """
        return Recipe.objects.filter(likes=self.request.user)
