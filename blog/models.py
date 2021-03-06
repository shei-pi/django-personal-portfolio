from django.db import models

class BlogPost(models.Model):
    
    title = models.CharField(max_length=50)
    publishing_date = models.DateField()
    content = models.TextField()
    
    def __str__(self):
        return self.title