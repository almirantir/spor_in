from django import forms
from pari.models import *


#форма для проверки ключа активации

class ActivationForm(forms.Form):

	key_act = forms.CharField(max_length=128)








