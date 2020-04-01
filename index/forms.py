from django import forms
from .models import Character, Comment, CharacterComment, Author

class DreamHeroForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name of your hero'

    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Story of your Hero at least 4 word'

    }))
    slug = forms.SlugField()
    hero_image = forms.ImageField()
    strenght = forms.IntegerField()
    power = forms.IntegerField()
    weapon = forms.IntegerField()

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        num_word = len(description.split())
        if num_word < 4:
            raise forms.ValidationError("Not enough words!")
        return description


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)

class CharCommentForm(forms.ModelForm):
    class Meta:
        model = CharacterComment
        fields = ('message',)


class AuthorProfForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('image', 'cover_image', 'bio', 'gender')





