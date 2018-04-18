#!/usr/bin/env python
# -*-coding:utf-8-*-

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='邮件主题')
    email = forms.EmailField(required=False, label='收件地址')
    message = forms.CharField(widget=forms.Textarea, label='邮件正文')

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("输入字符应当大于4个字符")
        return  message