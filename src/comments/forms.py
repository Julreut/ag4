from django import forms
from .models import Comment
from django.utils.translation import ugettext_lazy

class CommentModelForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': 3,
                'placeholder': ugettext_lazy("comment_creation_prompt"),
                'style': 'background-color: #F0F2F5;'
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('content',)


class SecondaryCommentModelForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': ugettext_lazy("reply_creation_prompt"),
                'style': 'background-color: #F0F2F5;'
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('content',)
