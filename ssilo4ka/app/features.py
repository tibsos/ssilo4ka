from django.db import models as m

class RedirectLink(m.Model):
    TIMEZONES=(
    ('+2','+2 UTC | Калининградское время'),
    ('+3','+3 UTC | Московское время'),
)
    end_date=m.DateField()
    end_time=m.TimeField()
    timezone=m.CharField(max_length=3,choices=TIMEZONES,default='+3')

    created_at=m.DateTimeField(auto_now_add=True)
    updated_at=m.DateTimeField(auto_now=True)

    def __str__(self):
        return ("Until "+str(self.end_date)+' '+str(self.end_time))
    class Meta:
        ordering=['end_date','end_time']