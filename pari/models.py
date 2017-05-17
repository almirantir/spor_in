from django.db import models



# абстрактный класс пользователя

class User(models.Model):
	email_send = models.EmailField()
	name_send = models.CharField(max_length=128)
	email_addres = models.EmailField()
	name_addres = models.CharField(max_length=128)

	class Meta:
		abstract = True


# основной класс спора
class Bet(User):
	
	bet_name = models.CharField(max_length=128)
	bet_body = models.TextField(blank=True, null=True, default=None)
	bet_end = models.DateField(auto_now_add=False, auto_now=False)
	bet_status = models.BooleanField(default=False)
	active_code = models.CharField(max_length=128, null=True, blank=True)

	def __str__(self):
		return "Спор %s " % (self.bet_name,)

	class Meta:
		verbose_name = 'Спорин'
		verbose_name_plural = 'Спорин'




	
