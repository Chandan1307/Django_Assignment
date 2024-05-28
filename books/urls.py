# books/urls.py
from django.urls import path
from .views import BookSearchView
from .views import BookRecommendationListCreateView


urlpatterns = [
    path('search/', BookSearchView.as_view(), name='book-search'),
    path('recommendations/', BookRecommendationListCreateView.as_view(), name='book-recommendations'),

]
