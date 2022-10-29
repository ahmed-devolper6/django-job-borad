from django import forms

from .models import Apply , Jobs




class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name' ,'email','cover_letter']



class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
        exclude = ('user',)