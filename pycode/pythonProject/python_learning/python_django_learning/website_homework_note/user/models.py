from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField('用户名', max_length=40, unique=True)
    password = models.CharField('密码', max_length=40)

    def __str__(self):
        return f'用户：{self.name}'
