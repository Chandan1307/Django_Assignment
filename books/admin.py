from django.contrib import admin
from .models import BookRecommendation

@admin.register(BookRecommendation)
class BookRecommendationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'recommended_by', 'rating', 'created_at')
    search_fields = ('title', 'author', 'recommended_by')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)
