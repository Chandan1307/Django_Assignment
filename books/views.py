# books/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_books
from .models import BookRecommendation
from .serializers import BookRecommendationSerializer
from rest_framework import generics

class BookSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        if not query:
            return Response({"error": "Query parameter 'q' is required"}, status=status.HTTP_400_BAD_REQUEST)
        books = fetch_books(query)
        return Response(books)

class BookRecommendationListCreateView(generics.ListCreateAPIView):
    queryset = BookRecommendation.objects.all()
    serializer_class = BookRecommendationSerializer
