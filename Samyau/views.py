# coding:utf-8
from django.shortcuts import render_to_response
import datetime


# def index(request):
#     now = datetime.datetime.now()
#     t = get_template('home.html')
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)


def index(request):
    current_date = datetime.datetime.now()
    return render_to_response('hr.html', locals())
