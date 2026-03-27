from django.urls import path
from .views import NewsList, NewsDetailView, SearchNews

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('search/', SearchNews.as_view(), name='news_search'),
]
