from django.contrib import admin
from .models import *

#создает админку для основной модели

class BetAdmin (admin.ModelAdmin):
	list_display = [field.name for field in Bet._meta.fields]

	class Meta:
		model = Bet

admin.site.register(Bet, BetAdmin)