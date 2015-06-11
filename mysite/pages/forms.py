from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import PageItem

class PageItemForm(forms.ModelForm):
    class Meta:
        model = PageItem
        fields = ('creator', 'name', 'fb_id', 'last_like_count', 'picture_url', 'notes',)
        widgets = {'last_like_count': forms.HiddenInput}

    def __init__(self, *args, submit_title='Submit', **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        if submit_title:
            self.helper.add_input(Submit('submit', submit_title))
