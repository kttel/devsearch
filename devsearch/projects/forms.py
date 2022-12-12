from django.forms import ModelForm
from django import forms
from . import models


class ProjectForm(ModelForm):
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'featured_image',
                  'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add your comment'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
