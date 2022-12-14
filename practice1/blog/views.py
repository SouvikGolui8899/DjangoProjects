from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleForm
from .models import Article

# Create your views here.

class ArticleCreateView(CreateView):
    template_name = 'article/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html
    # success_url = '<path>'

    def form_valid(self, form):
        return super().form_valid(form)

    # def get_success_url(self):
    #     return <something>


class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = 'article/article_detail.html'
    # queryset = Article.objects.all()  # <blog>/<modelname>_detail.html (default usage)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
    

class ArticleUpdateView(UpdateView):
    template_name = 'article/article_create.html'
    form_class = ArticleForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'article/article_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article_list')