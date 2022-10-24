from django import forms as f
from django.forms import ChoiceField
from user.models import Profile
from .features import RedirectLink

class AvatarForm(f.ModelForm):
    avatar=f.ImageField(widget=f.FileInput(attrs={'id':'avatar-form','class':'avatar-form'}))
    class Meta:
        model=Profile
        fields=('avatar',)

class DateInput(f.DateInput):
    input_type='date'

class TimeInput(f.TimeInput):
    input_type='time'
