from django import forms
from django.core.validators import RegexValidator


class ArtRequestForm(forms.Form):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
    ]
    openai_api_key = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "OpenAI API Key"}),
        max_length=100,
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    primary_color = forms.CharField(
        max_length=7,
        widget=forms.TextInput(attrs={"placeholder": "#ffffff"}),
        validators=[
            RegexValidator(
                regex="^#[A-Fa-f0-9]{6}$",
                message="Enter a valid hex color code, for example ",  # ffffff"
            )
        ],
    )
    props = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Prop1, Prop2, Prop3"}),
        validators=[
            RegexValidator(
                regex="^[^,]+(,[^,]+){0,2}$",
                message="Enter up to 3 props separated by commas, for example 'laptop, coffee mug, notebook'",
            )
        ],
    )
