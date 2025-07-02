from django.db import models
from user.models import User
# Create your models here.


class Note(models.Model):
    title = models.CharField('标题', max_length=40)
    content = models.TextField('内容')
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    update_date = models.DateTimeField('更新时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'标题：{self.title}'
