from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Recipe, Pantry
from .forms import InstructionForm, UserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def recipe_index(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipes/index.html', {'recipes': recipes})

@login_required
def recipe_detail(request, recipe_id):
    try:
        recipe = Recipe.objects.get(user=request.user, id=recipe_id)
        pantry = Pantry.objects.all()

    except Recipe.DoesNotExist:
        return redirect('recipe_create')
    instruction_form = InstructionForm()
    pantry_recipe_doesnt_have = Pantry.objects.exclude(id__in = recipe.pantry.all(). values_list('id'))
    return render(request, 'recipes/detail.html', {'recipe': recipe, 'instruction_form': instruction_form, 'pantry': pantry_recipe_doesnt_have})

class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'cuisine', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['name', 'cuisine', 'description']

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipes/'

@login_required
def add_instruction(request, recipe_id):
    form = InstructionForm(request.POST)
    if form.is_valid():
        new_instruction = form.save(commit=False)
        new_instruction.recipe_id = recipe_id
        new_instruction.save()
    return redirect('recipe_detail', recipe_id=recipe_id)

class PantryCreate(CreateView):
    model = Pantry
    fields = '__all__'

class PantryList(ListView):
    model = Pantry

class PantryDetail(DetailView):
    model = Pantry

class PantryUpdate(UpdateView):
    model = Pantry
    fields = '__all__'

class PantryDelete(DeleteView):
    model = Pantry
    success_url = '/pantry/'

def associate_pantry(request, recipe_id, pantry_id):
    Recipe.objects.get(id=recipe_id).pantry.add(pantry_id)
    return redirect('recipe_detail', recipe_id=recipe_id)

def remove_pantry(request, recipe_id, pantry_id):
    Recipe.objects.get(id=recipe_id).pantry.remove(pantry_id)
    return redirect('recipe_detail', recipe_id=recipe_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
