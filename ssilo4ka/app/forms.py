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


class RedirectDateTimeForm(f.Form):
    date=f.DateField(widget=DateInput(attrs={'id':'redirect-date'}))
    time=f.TimeField(widget=TimeInput(attrs={'id':'redirect-time'}))


class TimezoneForm(f.ModelForm):
    gender = ChoiceField(widget=f.Select(attrs={'onChange':'updateTimezone();'}))
    class Meta:
        model=RedirectLink
        fields=('timezone',)
