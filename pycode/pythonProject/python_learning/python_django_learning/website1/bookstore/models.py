from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=20, unique=True, verbose_name="书名")
    pub = models.CharField(max_length=40)
    price = models.FloatField()
    market_price = models.FloatField()

    def __str__(self):
        return f"书名：{self.title}"

    class Meta:
        verbose_name = "Book单数名"
        verbose_name_plural = "Book复数名"

class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=1)
    email = models.EmailField(blank=True)
