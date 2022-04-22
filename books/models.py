from django.db import models

# Create your models here.


BOOK_CATEGORY = (
    ("Health", "Health"),
    ("Technology", "Technology"),
    ("Games", "Games"),
    ("Meetups", "Meetups"),
    ("Music", "Music"),
    ("Art", "Art"),
    ("Food", "Food"),
    ("Business", "Business"),
    ("Sports", "Sports"),
)


PAYMENT_TYPE = (
    ("Cash", "Cash"),
    ("Card", "Card"),
    ("UPI", "UPI"),
)

class Book(models.Model):
	title = models.CharField(max_length=80)
	author = models.CharField(max_length=80)
	price = models.CharField(max_length=12)
	category = models.CharField(max_length=20, choices=BOOK_CATEGORY)
	date_added = models.DateField(auto_now_add=True)
	is_available = models.BooleanField(default=True)

	def __str__(self):
		return str(self.title)


class Orders(models.Model):
	user_id = models.ForeignKey('user.User', on_delete=models.PROTECT)
	book_id = models.ForeignKey(Book, on_delete=models.PROTECT)
	payment_method = models.CharField(max_length=20, choices=PAYMENT_TYPE)
	amount = models.PositiveIntegerField()
	deliver = models.BooleanField(default=False)
	order_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user)
