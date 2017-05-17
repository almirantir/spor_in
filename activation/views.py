# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.edit import FormView
from .forms import *



# проверяет ключ активации пари 

def activation(request):

	form = ActivationForm(request.POST or None)

	if request.method == "POST" and form.is_valid():
		key_act = form.cleaned_data['key_act']
		
		try:
			spor = Bet.objects.get(active_code = key_act)
			spor.bet_status = True
			spor.save()
			return render (request, './true_act.html', locals())
			
		except Bet.DoesNotExist:
			return render (request, './act_error.html', locals())

	return render (request, './activation.html', locals())










