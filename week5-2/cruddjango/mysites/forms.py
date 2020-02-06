from django import forms
from .models import WritingContents

class ContentsForm(forms.ModelForm):
    class Meta:
        model = WritingContents
        fields = ('title', 'contents', 'price', 'score',)
        #Forms.py Widget Setting