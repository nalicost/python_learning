from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name="用户名", max_length=30, unique=True)
    password = models.CharField(verbose_name="密码", max_length=30)

    def __str__(self):
        return f"用户名：{self.name}"
