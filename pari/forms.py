from django import forms
from .models import *


# наследуем от основной модели спора

class BetForm(forms.ModelForm):

	class Meta:
		model = Bet
		exclude = ['bet_status', 'active_code']







