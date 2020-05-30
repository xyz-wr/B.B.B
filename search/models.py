from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True)
    pub_date = models.DateField()
    content = models.TextField('CONTENT')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        
    def __str__(self ):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(slef.slug,))