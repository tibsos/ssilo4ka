from django.db import models as m

class Link(m.Model):

    title=m.CharField(max_length=50,blank=True,null=True)
    url=m.URLField(max_length=3000,blank=True,null=True)
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

    blockType=m.CharField(max_length=20,choices=BLOCK_TYPE,default='link')
    active=m.BooleanField(default=True)
    link=m.ForeignKey(Link,on_delete=m.DO_NOTHING)

    createdAt=m.DateTimeField(auto_now_add=True)
    updatedAt=m.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blockType or None
    class Meta:
        ordering=['updatedAt']