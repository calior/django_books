# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='公司名称')
    address = models.CharField(max_length=50, verbose_name='公司地址')
    city = models.CharField(max_length=60, verbose_name='所在城市')
    state_provice = models.CharField(max_length=30, verbose_name='所在省份', default='')
    country = models.CharField(max_length=50, verbose_name='所在国家', default='')
    website = models.URLField(verbose_name='官网地址', default='')

    def __unicode__(self):

        # return u'name=%s' \
        #        u'address=%s' \
        #        u'city=%s' \
        #        u'state_provice=%s' \
        #        u'contry=%s' \
        #        u'website=%s' % (self.name, self.address, self.city, self.state_provice, self.country, self.website)
        return self.name
    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = "出版社"

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓 名', default='')
    # last_name = models.CharField(max_length=40, verbose_name='名')
    email = models.EmailField(blank=True, verbose_name='邮 箱')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = "作者"

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='书 名')
    author = models.ManyToManyField(Author, verbose_name='作 者')
    publisher = models.ForeignKey(Publisher, verbose_name='出版商')
    publisher_date = models.DateField(blank=True, null=True, verbose_name='出版日期')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "书 名"
        verbose_name_plural = "书 名"

class Contact(models.Model):
    subject = models.CharField(max_length=128, verbose_name='邮件主题')
    email = models.EmailField(blank=True, verbose_name='收件地址')
    message = models.TextField(verbose_name='邮件正文')

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = "联系我们"
        verbose_name_plural = "联系我们"
