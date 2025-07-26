from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipe_index, name='recipe_index'),
    path('recipes/<int:recipe_id>', views.recipe_detail, name='recipe_detail'), 
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'),
    path('recipes/<int:recipe_id>/add-instruction/', views.add_instruction, name="add_instruction"),
    path('pantry/create/', views.PantryCreate.as_view(), name="pantry_create"),
    path('pantry/<int:pk>/', views.PantryDetail.as_view(), name="pantry_detail"),
    path('pantry/', views.PantryList.as_view(), name="pantry_index"),
    path('pantry/<int:pk>/update', views.PantryUpdate.as_view(), name='pantry_update'),
    path('pantry/<int:pk>/delete', views.PantryDelete.as_view(), name='pantry_delete'),
    path('recipes/<int:recipe_id>/associate-pantry/<int:pantry_id>/', views.associate_pantry, name="associate_pantry"),
    path('recipes/<int:recipe_id>/remove-pantry/<int:pantry_id>/', views.remove_pantry, name="remove_pantry"),

    path('accounts/signup', views.signup, name='signup'),
]