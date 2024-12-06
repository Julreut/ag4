from django import forms

from profiles.models import Profile
from articles.models import Article

class APIProfileModelForm(forms.ModelForm):
    avatar = forms.ImageField(label='', required=True)
    class Meta:
        model = Profile
        fields = ('avatar',)

class APIArticleModelForm(forms.ModelForm):
    image = forms.ImageField(label='', required=True)
    
    class Meta:
        model = Article
        fields = ('image',)

class APICommentModelForm(forms.ModelForm):
    image = forms.ImageField(label='', required=True)
    
    class Meta:
        model = Article
        fields = ('image',)
