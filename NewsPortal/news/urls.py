from django.urls import path
from .views import (NewsList, NewsDetail, PostSearch, NewsCreate, NewsUpdate, NewsDelete,
                    ArticlesCreate, ArticlesUpdate, ArticlesDelete)

urlpatterns = [
    path('', NewsList.as_view(), name='news list'),
    path('<int:pk>', NewsDetail.as_view(), name='news detail'),
    path('search/', PostSearch.as_view()),
    path('news/create/', NewsCreate.as_view(), name='news create'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news delete'),
    path('articles/create/', ArticlesCreate.as_view(), name='articles create'),
    path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='articles update'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles delete'),
]