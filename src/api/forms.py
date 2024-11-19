from django import forms

from posts.models import Post
from profiles.models import Profile
from advertisements.models import Advertisement
from articles.models import Article, NewsPaper


class APIAdvertisementModelForm(forms.ModelForm):
    image = forms.ImageField(label='', required=True)
    class Meta:
        model = Advertisement
        fields = ('image',)

class APIPostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)

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
