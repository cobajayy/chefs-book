from django.contrib import admin
from .models import Recipe, Instruction, Pantry

admin.site.register(Recipe)
admin.site.register(Instruction)
admin.site.register(Pantry)