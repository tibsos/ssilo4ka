from django import forms as f
from user.models import Profile

class AvatarForm(f.ModelForm):
    avatar=f.ImageField(widget=f.FileInput(attrs={'id':'avatar-form','class':'avatar-form'}))
    class Meta:
        model=Profile
        fields=('avatar',)