from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Task


class LoginForm(forms.Form):
    
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password1', 'password2', 'is_excom', 'is_director', 'is_member')

class TaskForm(forms.ModelForm):
	# CompletedTask = forms.BooleanField()
    # taskcom = forms.BooleanField(widget=forms.NullBooleanSelect(attrs={ 'style': 'width: 10px; height: 10px', 'class': 'form-control'}))
    # complete = forms.DateField(widget=forms.DateInput(attrs={'placeholder' :'Completion Date', 'style': 'width: 300px;', 'class': 'form-control'}))

	class Meta:
		model = Task
		fields = ['taskcom','completion_date']
        