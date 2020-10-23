from django.db import models


# Create your models here.
class publisher(models.Model):
    name = models.CharField(max_length=32)


class Book(models.Model):
    name = models.CharField(max_length=32)
    publisher = models.ForeignKey(publisher, on_delete=models.CASCADE)  #默认是级联删除
    # authors = models.ManyToManyField('Author')
    """
    on_delete
        models.CASCADE  级联删除
        models.PROTECT 保护
        models.SET(v) 删除后设置为默认值
        models.SETDEFAULT  删除后设置为默认值
        models.SET_NULL  删除后设置为Null
    """


class author(models.Model):
    name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book') #不在author表中创建字段，会创建第3张表

