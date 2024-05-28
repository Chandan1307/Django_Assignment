from django.db import models

class BookRecommendation(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.URLField()
    rating = models.FloatField()
    recommended_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
