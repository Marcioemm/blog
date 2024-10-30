from django.db import models
from datetime import datetime



class Tag(models.Model):

    name = models.CharField(max_length=50,null=False, blank=False)

    
    class Meta:
        db_table = 'blog_tag'

    def __str__(self):
        return self.name    

    


class Post(models.Model):

    title = models.TextField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(blank=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        db_table = 'blog_post'

    def __str__(self):
        return self.title




