from django import forms
from .models import Instruction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['step', 'instruction']

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']