from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_queryset(self):
        return Post.objects.filter().order_by('-dateCreation')


class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'