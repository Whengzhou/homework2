from django import forms
from django.contrib.auth.models import User
from firstapp.models import UserProfile


from django.core.exceptions import ValidationError


def word_validator(comment):
    if len(comment) < 4:
        raise ValidationError("not enough words")


def comment_validator(comment):
    keywords = [u"发票", u"钱"]
    for keyword in keywords:
        if keyword in comment:
            raise ValidationError("Your comment contains invalid words,please check it again.")


class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages = {
            "required": 'wow, such words'
            },
        validators = [word_validator, comment_validator]
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'sex', 'avatar']


class PasswordForm(forms.Form):
    password = forms.CharField(label=(u"新密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))
