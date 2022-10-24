from django.shortcuts import render

import datetime as dt
import calendar as cal

def calendar(request):
    c={}
    current_month_days=cal.monthcalendar(dt.datetime.now().year,dt.datetime.now().month)
    c['days']=current_month_days
    return render(request,'calendar/calendar.html',c)