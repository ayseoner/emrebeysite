from django import forms
from .models import Post , Post2 , Post3

from django.forms import ModelForm



class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsminiz'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Konu'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon'})

        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-element'

class PostForm2(ModelForm):

    class Meta:
        model = Post2
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsminiz'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Konu'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon'}),
            'message': forms.TextInput(attrs={'placeholder': 'Mesajınız'})

        }

    def __init__(self, *args, **kwargs):
        super(PostForm2, self).__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-element'

class PostForm3(ModelForm):

    class Meta:
        model = Post3
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsminiz'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon Numaranız'}),

        }

    def __init__(self, *args, **kwargs):
        super(PostForm3, self).__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-element'





