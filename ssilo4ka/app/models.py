from django.db import models as m
from uuid import uuid4 as u4

from app.analytics import LinkActivity

class Link(m.Model):
    block=m.ForeignKey('Block',on_delete=m.CASCADE,related_name='link_block')
    title=m.CharField(max_length=50,blank=True,null=True)
    url=m.CharField(max_length=3000,blank=True,null=True)
    activity=m.ManyToManyField(LinkActivity,blank=True)

    def __str__(self):
        return self.title or "undefined"

    class Meta:
        ordering=['title']

class Block(m.Model):

    BLOCK_TYPE=(
        ('link','Ссылка'),
        ('section','Раздел'),
        ('video','Видео'),
        ('music','Музыка'),
        ('document','Документ'),
        ('VKpub','ВК паблик'),
        ('TikTok Video','Видео из ТикТока'),
        ('Twitch','Twitch'),
        ('podcasts','Подкасты'),
        ('nft gallery','NFT Галерея'),
        ('Ymusic','Яндекс Музыка'),
        ('soundcloud','SoundCloud'),
        ('tips','Чаевые'),
        ('mobile app','Мобильное Приложение'),
    )

    uid=m.UUIDField(default=u4)

    active=m.BooleanField(default=True)

    blockType=m.CharField(max_length=20,choices=BLOCK_TYPE,default='link')
    link=m.ForeignKey(Link,on_delete=m.DO_NOTHING,blank=True,null=True,related_name="blocks_link")

    createdAt=m.DateTimeField(auto_now_add=True)
    updatedAt=m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blockType
    class Meta:
        ordering=['updatedAt']