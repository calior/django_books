# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-14 02:09
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, null=True, unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('realname', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u771f\u5b9e\u59d3\u540d')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('dept', models.CharField(choices=[('\u6d4b\u8bd5', '\u6d4b\u8bd5'), ('\u5f00\u53d1', '\u5f00\u53d1')], max_length=100, verbose_name='\u90e8\u95e8')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u6fc0\u6d3b\u72b6\u6001')),
                ('is_admin', models.BooleanField(default=False, verbose_name='\u662f\u5426\u7ba1\u7406\u5458')),
                ('testrailuser', models.CharField(blank=True, max_length=50, null=True, verbose_name='TestRail\u7528\u6237\u540d')),
                ('testrailpass', models.CharField(blank=True, max_length=50, null=True, verbose_name='TestRail\u5bc6\u7801')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testrailcaseid', models.CharField(blank=True, max_length=12, null=True)),
                ('casedesc', models.CharField(max_length=255, verbose_name='Title')),
                ('isenabled', models.BooleanField(default=True)),
                ('issmoke', models.BooleanField(default=False)),
                ('dependent', models.CharField(blank=True, max_length=8, null=True)),
                ('debuginfo', models.CharField(blank=True, max_length=9999, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now_add=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Caseset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(max_length=200)),
                ('caseid', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('isenabled', models.BooleanField(default=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Codelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=32)),
                ('codedescr', models.CharField(max_length=255)),
                ('codevalue', models.CharField(max_length=255)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descr', models.CharField(max_length=100)),
                ('locmode', models.CharField(blank=True, choices=[('id', 'id'), ('name', 'name'), ('css selector', 'css selector'), ('xpath', 'xpath'), ('class_name', 'class name'), ('tag_name', 'tag name'), ('link_text', 'link text'), ('portial_link_text', 'portial link text')], max_length=32, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(blank=True, null=True, verbose_name='\u6240\u5c5e\u4ea7\u54c1')),
                ('keyword', models.CharField(max_length=32, unique=True)),
                ('kwdescr', models.TextField(blank=True, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'ordering': ['productid'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u6a21\u5757\u540d\u79f0')),
                ('isenabled', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('createat', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u521b\u5efa\u8005')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updateat', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u66f4\u65b0\u8005')),
                ('sortby', models.IntegerField(blank=True, default=0, null=True, verbose_name='\u6392\u5e8f')),
            ],
            options={
                'ordering': ['-sortby'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('isenabled', models.BooleanField(default=True, verbose_name='\u4ea7\u54c1\u72b6\u6001')),
                ('descr', models.TextField(blank=True, null=True, verbose_name='\u4ea7\u54c1\u63cf\u8ff0')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('createat', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u521b\u5efa\u8005')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updateat', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u66f4\u65b0\u8005')),
                ('sortby', models.IntegerField(blank=True, default=0, null=True, verbose_name='\u6392\u5e8f')),
            ],
            options={
                'ordering': ['-sortby'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('version', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7248\u672c')),
                ('isenabled', models.BooleanField(default=True, verbose_name='\u72b6\u6001')),
                ('descr', models.TextField(blank=True, null=True, verbose_name='\u9879\u76ee\u63cf\u8ff0')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('createat', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u521b\u5efa\u8005')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updateat', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u66f4\u65b0\u8005')),
                ('sortby', models.IntegerField(blank=True, default=0, null=True, verbose_name='\u6392\u5e8f')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Product', verbose_name='\u4ea7\u54c1\u540d\u79f0')),
            ],
            options={
                'ordering': ['-sortby'],
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stepid', models.IntegerField(blank=True, null=True)),
                ('descr', models.CharField(blank=True, max_length=200, null=True)),
                ('inputtext', models.CharField(blank=True, max_length=200, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
                ('caseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Case')),
                ('elementid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autoplat.Element')),
                ('keywordid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=255, verbose_name='\u4efb\u52a1\u63cf\u8ff0')),
                ('tasktype', models.CharField(blank=True, choices=[('1', '\u6267\u884c\u7528\u4f8b'), ('2', '\u7528\u4f8b\u540c\u6b65'), ('3', '\u5173\u8054Jenkins')], max_length=32)),
                ('status', models.SmallIntegerField(default=0, verbose_name='\u4efb\u52a1\u72b6\u6001')),
                ('issmoke', models.BooleanField(default=False)),
                ('testrailsuites', models.CharField(blank=True, max_length=8, null=True, verbose_name='TestRail\u6d4b\u8bd5\u96c6ID')),
                ('testrailrunid', models.CharField(blank=True, max_length=8, null=True, verbose_name='TestRail\u6267\u884cID')),
                ('testsectionid', models.CharField(blank=True, max_length=8, null=True, verbose_name='TestRail\u7528\u4f8b\u8282\u70b9ID')),
                ('jenkins_server_url', models.CharField(blank=True, max_length=100, null=True, verbose_name='JenkinsServer')),
                ('user_id', models.CharField(blank=True, max_length=32, null=True, verbose_name='JenkinsUserid')),
                ('api_token', models.CharField(blank=True, max_length=32, null=True, verbose_name='JenkinsApitoken')),
                ('build_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='JenkinsBuildName')),
                ('caselist', models.CharField(max_length=10240, verbose_name='\u7528\u4f8b\u5217\u8868')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('createat', models.CharField(blank=True, max_length=32, null=True)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('updateat', models.CharField(blank=True, max_length=32, null=True)),
                ('projectid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Taskhistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasktype', models.CharField(blank=True, max_length=32)),
                ('taskname', models.CharField(max_length=255, verbose_name='\u4efb\u52a1\u63cf\u8ff0')),
                ('case_tag_all', models.CharField(blank=True, max_length=8, null=True)),
                ('case_tag_pass', models.CharField(blank=True, max_length=8, null=True)),
                ('case_tag_fail', models.CharField(blank=True, max_length=8, null=True)),
                ('case_tag_error', models.CharField(blank=True, max_length=8, null=True)),
                ('starttime', models.DateTimeField(blank=True)),
                ('exectime', models.CharField(blank=True, max_length=32, null=True)),
                ('reporturl', models.CharField(max_length=255, null=True, verbose_name='report Url')),
                ('build_name', models.CharField(blank=True, max_length=32, null=True)),
                ('build_number', models.CharField(blank=True, max_length=8, null=True)),
                ('taskid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Task')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserandProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='projectid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Project', verbose_name='\u6240\u5c5e\u9879\u76ee'),
        ),
        migrations.AddField(
            model_name='element',
            name='moduleid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Module'),
        ),
        migrations.AddField(
            model_name='element',
            name='projectid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Project'),
        ),
        migrations.AddField(
            model_name='codelist',
            name='taskid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Task'),
        ),
        migrations.AddField(
            model_name='case',
            name='moduleid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Module'),
        ),
        migrations.AddField(
            model_name='case',
            name='projectid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoplat.Project'),
        ),
    ]
