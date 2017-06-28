from django.db import models

# Create your models here.
class Search(models.Model):
    keys = models.CharField(max_length=50, verbose_name=u'关键词')
    contentType = models.CharField(max_length=20, verbose_name=u'类型')

    class Meta:
        verbose_name = u'搜索'
        verbose_name_plural = verbose_name