from django.db import models as m
from django.utils.translation import gettext_lazy as _

class PageStatistics(m.Model):
    total_views=m.PositiveIntegerField(_("Всего просмотров страницы"),default=0)
    total_clicks=m.PositiveIntegerField(_("Всего кликов по кнопкам"),default=0)
    total_time_spent=m.PositiveIntegerField(_("Время проведнное на странице [с]"),default=0)
    average_time=m.PositiveIntegerField(_("Среднее проведенное время на странице [с]"),default=0)
    average_time_2click=m.PositiveIntegerField(_("Среднее проведенное время до клика на кнопку [с]"),default=0)

    class Meta:
        verbose_name='Статистика ссылочки'
        verbose_name_plural='Статистика ссылочек'
    class Meta:
        ordering=['total_views']

    @property
    def ctr(self):
        clicks=self.total_clicks
        views=self.total_views
        if views!=0 and clicks!=0:
            return str(round(clicks/views*100,ndigits=2))+'%'
        elif views!=0 and clicks==0:
            return '0%'
        else:
            return '-'

    @property
    def views(self):
        views=self.total_views
        if views<1000:
            return str(views)
        if views>1000 and views<1000000:
            return str(round(views/1000,ndigits=2))+'K'
        if views>1000000:
            return str(round(views/1000000,ndigits=2))+'M'

    @property
    def clicks(self):
        clicks=self.total_clicks
        if clicks<1000:
            return str(clicks)
        if clicks>1000 and clicks<1000000:
            return str(round(clicks/1000,ndigits=2))+'K'
        if clicks>1000000:
            return str(round(clicks/1000000,ndigits=2))+'M'

    @property
    def time_spent(self):
        seconds=self.total_time_spent  
        if seconds<60:
            return str(seconds)    
        if seconds>60 and seconds<3600:
            minutes=seconds//60
            seconds=seconds-minutes*60
            if seconds==0:
                return (str(minutes)+"м")
            else:
                return (str(minutes)+"м "+str(seconds)+'с')
        if seconds>3600:
            hours=seconds//3600
            seconds-=hours*3600
            minutes=seconds//60
            seconds=seconds-minutes*60
            if minutes>0 and seconds>0:
                return (str(hours)+'ч '+str(minutes)+"м "+str(seconds)+'с')
            elif minutes>0 and seconds==0:
                return (str(hours)+'ч '+str(minutes)+"м ")
            elif minutes==0 and seconds>0:
                return (str(hours)+'ч '+str(seconds)+'с')
            else:
                return (str(hours)+'ч')
        else:
            return ('0с')

    @property
    def avrg_time_spent(self):
        seconds=self.average_time_spent
        if seconds<60:
            return str(seconds)    
        if seconds>60 and seconds<3600:
            minutes=seconds//60
            seconds=seconds-minutes*60
            if seconds==0:
                return (str(minutes)+"м")
            else:
                return (str(minutes)+"м "+str(seconds)+'с')
        if seconds>3600:
            hours=seconds//3600
            seconds-=hours*3600
            minutes=seconds//60
            seconds=seconds-minutes*60
            if minutes>0 and seconds>0:
                return (str(hours)+'ч '+str(minutes)+"м "+str(seconds)+'с')
            elif minutes>0 and seconds==0:
                return (str(hours)+'ч '+str(minutes)+"м ")
            elif minutes==0 and seconds>0:
                return (str(hours)+'ч '+str(seconds)+'с')
            else:
                return (str(hours)+'ч')
        else:
            return ('0с')

    @property
    def avrg_time_2click(self):
        seconds=self.average_time_2click
        if seconds<60:
            return str(seconds)    
        if seconds>60 and seconds<3600:
            minutes=seconds//60
            seconds=seconds-minutes*60
            if seconds==0:
                return (str(minutes)+"м")
            else:
                return (str(minutes)+"м "+str(seconds)+'с')
        if seconds>3600:
            hours=seconds//3600
            seconds-=hours*3600
            minutes=seconds//60
            seconds=seconds-minutes*60
            if minutes>0 and seconds>0:
                return (str(hours)+'ч '+str(minutes)+"м "+str(seconds)+'с')
            elif minutes>0 and seconds==0:
                return (str(hours)+'ч '+str(minutes)+"м ")
            elif minutes==0 and seconds>0:
                return (str(hours)+'ч '+str(seconds)+'с')
            else:
                return (str(hours)+'ч')
        else:
            return ('0с')

class PageActivity(m.Model):
    ip_address=m.CharField(max_length=20,blank=True,null=True)
    visit_duration=m.PositiveIntegerField(_("Время визита [s]"),)
    referral=m.CharField(max_length=10,blank=True,null=True)
    visited_at=m.DateTimeField(_("Момент визита"),auto_now_add=True)
    class Meta:
        verbose_name='Активность на ссылочке'
        verbose_name_plural='Активность на ссылочках'

class LinkActivity(m.Model):
    ip_address=m.CharField(max_length=20,blank=True,null=True)
    time_2click=m.PositiveIntegerField(_("Время проведенное до клика на кнопку [s]"),)
    clicked_at=m.DateTimeField(_("Момент нажатия"),auto_now_add=True)
    class Meta:
        verbose_name='Активность блока'
        verbose_name_plural='Активность блоков'

class ProfileActivity(m.Model):
    page=m.CharField(max_length=100)
    next_page=m.CharField(max_length=100)
    referral=m.CharField(max_length=10,blank=True,null=True)
    visit_duration=m.PositiveIntegerField()
    visited_at=m.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Активность Профиля'
        verbose_name_plural='Активность Профилей'
            
class Activity(m.Model):
    ip_address=m.CharField(max_length=20,blank=True,null=True)
    page=m.CharField(max_length=20)
    referral=m.CharField(max_length=10,blank=True,null=True)
    visit_duration=m.PositiveIntegerField()
    visited_at=m.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Активность'
        verbose_name_plural='Активности'