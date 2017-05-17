# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.edit import FormView
from random import choice
from string import ascii_letters
from django.core.mail import *
from .forms import *

# получает спор и отправляет письмо с кодом активации второму спорщику
def bet(request):

	form = BetForm(request.POST or None)

	if request.method == "POST" and form.is_valid():
		post = form.save(commit=False)

		#генерируем уникальный ключ (active_code)
		post.active_code = ''.join(choice(ascii_letters) for i in range(12))
		
		#отправляем письмо с ключом второму пользователю
		mail_adr = [form.cleaned_data['email_addres']]
		subject = 'Вам предложили пари!'
		body = 'Код активации  %s Условия спора:  Дата окончания: %s Ссылка для активации' % (post.active_code, post.bet_body, str(post.bet_end))
		mail_from = '_________' # ваш аккаунт
		mail = EmailMessage(subject, body, mail_from, mail_adr)
		mail.content_subtype = "html"
		mail.send(fail_silently=False)

		print (request.POST)
		post.save()
		return render (request, './true_act.html', locals())

	return render(request, './pari.html', locals())









