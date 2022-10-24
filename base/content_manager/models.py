import os

from django.db import models as m

from uuid import uuid4 as u4

def upload_file(instance,filename):

    file_extension=filename.split('.')[-1]
    new_file_name=f"{u4}.{file_extension}"
    return os.path.join('uploads/content-manager/files',new_file_name)

CONTENT_TYPES=(
    ('bp','Blog Post'),
    ('smp','Social Media Post'),
)

CONTENT_STATUS=(
    ('ns','Not started'),
    ('ip','In progress'),
    ('pl','Published late'),
    ('f2p','Failed to publish'),
    ('p','Published'),
)

class Content(m.Model):

    title=m.CharField(max_length=300)
    description=m.TextField(max_length=1000)
    type=m.CharField(max_length=30,choices=CONTENT_TYPES)
    status=m.CharField(max_length=30,choices=CONTENT_TYPES)

    #post=CK # in case the content is a blog post

    start_date=m.DateField()
    start_time=m.TimeField()

    publish_date=m.DateField()
    publish_time=m.TimeField()

    created_at=m.DateTimeField(auto_now_add=True)
    updated_at=m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    ordering=['publish_date']

class File(m.Model):

    content=m.ForeignKey(Content,on_delete=m.CASCADE)
    
    title=m.CharField(max_length=300)

    file=m.FileField(upload_to=upload_file)
    
    created_at=m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "File for "+"'"+self.content.title+"'"
    class Meta:
        ordering=["content","created_at"]