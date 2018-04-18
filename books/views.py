# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
import smtplib
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.shortcuts import render, redirect
from books.models import *
from django.core.mail import send_mail
from books.forms import ContactForm
import os,sys
# Create your views here.


def test(request):

    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    # html = "<html><body>It is now %s</body></html>" % now
    # return HttpResponse(html)

    # now = datetime.datetime.now()
    #
    return render_to_response('book_list.html', locals())

def book_list(request):
    # sql = 'select name from books order by name;'
    # db = MySQLdb.connect(user='root', db='autoplat', passwd='root', host='127.0.0.1')
    # curror = db.cursor()
    # curror.execute(sql)
    # names = [row[0] for row in curror.fetchall()]
    # db.close()

    #p1 = Publisher.objects.filter(id=1).update(address='2855 Telegraph Avenue', city='Berkeley', \
    #                                            state_provice='CA', country='U.S.A', website='http://www.apress.com/')
    publisher = Publisher.objects.all()

    return render_to_response('book_list.html', locals())

def form_test(request):

    # a = request.META['REMOTE_ADD']

    # try:
    #     a = request.META['REMOTE_ADD']
    # except KeyError:
    #     a = 'unknown'

    value = request.META.items()
    value.sort()
    # html = []
    # for k, v in value:
    #     html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))


    # return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return render_to_response('request_header.html', locals())

def search(request):
    errors = []
    if 'q' in request.GET:#and request.GET.get('q'):
        q = request.GET.get('q')
        if not q:
            errors.append('提交内容不能空！')
        elif len(q) > 20:
            errors.append('提交内容不能超过20个字符！')
        else:
            books = Book.objects.filter(author__name__icontains=q)
            return render_to_response('search_result.html', {'books': books, 'query': q})
    # else:
    #     #flag = 'false'
    #     massage = '不能提交空表单'
    #     # return HttpResponse(massage)
    #     return render_to_response('search_form.html', {'massage': massage, 'flag': True})
    return render_to_response('search_form.html', {'errors': errors})

def contact(request):
    if request.method == 'POST':
        errors = []
        form = ContactForm(request.POST)
        # context_dict = {'errors': errors, 'subject': request.POST.get('subject', ''),
        #                 'message': request.POST.get('message', ''), 'email': request.POST.get('email', '')}
        # if not request.POST.get('subject', ''):
        #     errors.append('请输入邮件主题')
        #     return render(request, 'contact_form.html', context_dict)
        #     return render_to_response()
        # if '@' not in request.POST.get('email') or not request.POST.get('email'):
        #     errors.append('请输入有效的邮箱地址')
        #     return render(request, 'contact_form.html', context_dict)
        # if not request.POST.get('message', ''):
        #     errors.append('请输入邮件内容')
        #     return render(request, 'contact_form.html', context_dict)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                send_mail(
                    cd['subject'],
                    cd['email'],
                    cd['message'],
                    ['test@test.com'],
                    # cd.get('email', 'test@test.com'),
                    #['siteowner@example.com'],
                )
                # Contact.objects.create(subject=cd['subject'], email=cd['email'], message=cd['message'])
                contact = Contact()
                contact.subject = cd['subject']
                contact.email = cd['email']
                contact.message = cd['message']
                contact.save()
            except smtplib.SMTPException as e:
                errors.append(u"邮件发送失败: %s" % e)
                return HttpResponse(errors)

            subject = cd['subject']
            email = cd['email']
            message = cd['message']
            # return HttpResponseRedirect("/book/contact/thanks/?subject=%s&email=%s&message=%s" % (subject, email, message))
            return thanks(request, args={'subject': subject, 'email': email, 'message': message})
        # if not errors:
        #         #     try:
        #         #         send_mail(request.POST['subject'],
        #         #                   request.POST['message'],
        #         #                   request.POST.get('email', 'jzh.chen@hnair.com'),
        #         #                   ['jzh.chen@hnair.com'],
        #         #                   )
        #         #         return HttpResponseRedirect('/book/contact/thanks/')
        #         #     except :
        #         #         errors.append('邮件发送失败')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    context_dict = {'form': form}
    return render(request, 'contact_form.html', context_dict)

    #return render_to_response('contact_form.html', context_dict, context_instance=RequestContext(request))


def thanks(request,args=None):
    subject = args.get('subject')  # request.GET.get('subject')
    email = args.get('email')  # request.GET.get('email')
    message = args.get('message')  # request.GET.get('message')

    return render_to_response('contact_thanks.html', locals())