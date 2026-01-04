from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_url = models.URLField()
    live_demo_url = models.URLField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
