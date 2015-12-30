from django import forms
from django.db import models
class nameform(forms.Form):
	your_name = forms.CharField(label="Your Name",max_length=40)
