from django.db import models
from django.core.urlresolvers import reverse

class Songlist(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'songlist'
        verbose_name_plural = 'songlists'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('song:song_list_by_songlist', args=[self.slug])

class Song(models.Model):
    songlist = models.ForeignKey(Songlist, related_name='songs')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='songs/%Y/%m/%d', blank=True)
    count = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('song:song_detail', args=[self.id, self.slug])
