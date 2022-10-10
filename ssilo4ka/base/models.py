from django.db import models as m

class Link(m.Model):

    url=m.URLField(max_length=300З)

    def __str__(self):
        return self.url