# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
import datetime
from pari.models import *

def my_scheduled_job():

	now = datetime.datetime.now().date()
	fin = Bet.objects.get(bet_end = now)
	mail_adr = fin.email_send
	mail_adr2 = fin.email_addres

	subject = 'chron-tub'
	body = fin.bet_body
	mail_from = 'almirantir@gmail.com' # ваш аккааунт
	mail = EmailMessage(subject, body, mail_from, [mail_adr,mail_adr2])
	mail.content_subtype = "html"
	mail.send(fail_silently=False)
	pass