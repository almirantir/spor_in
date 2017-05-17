# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
import datetime
from django.core.exceptions import MultipleObjectsReturned
from pari.models import *


#  проверяет есть ли в базе  активные споры заканчивающиеся сегодня и отправляет сообщения участникам
# запускается django-crontab

def my_scheduled_job():


	now = datetime.datetime.now().date()
	
	try:
		for fin in Bet.objects.filter(bet_end = now , bet_status = True):
			
			fin.bet_status = False
			fin.save()
			
			mail_adr = fin.email_send
			mail_adr2 = fin.email_addres
			subject = 'Ваше пари подошло к концу!'
			body = fin.bet_body
			mail_from = '___________' # ваш аккаунт
			mail = EmailMessage(subject, body, mail_from, [mail_adr,mail_adr2])
			mail.content_subtype = "html"
			mail.send(fail_silently=False)

	except Bet.DoesNotExist:
		return None