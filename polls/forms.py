from django import forms
from .models import TeacherModel

class TeacherForm(forms.ModelForm):
    name_uz=forms.CharField()
    name_en=forms.CharField()
    name_ru=forms.CharField()

    class Meta:
        model=TeacherModel
        exclude=('name',)