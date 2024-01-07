from django import forms
from django.forms import ModelForm  
from widepen.models import User, Post


categories = [('python', 'Python'), ('data science', 'Data Science'), ('excel', 'Excel'), ('machine learning', 'Machine Learning'), ('deep learning', 'Deep Learning')]


class post_form(ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'category',
            'story',
            
        )

        labels ={
            'title':'',
            'category':'',
            'story':'',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control title', 'placeholder':'Title'}),
            'category': forms.Select(choices=categories, attrs={'class':'form-control'}),
            'story': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Story'}),
        }


class profile_edit_form(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'bio', 'profile_picture']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }