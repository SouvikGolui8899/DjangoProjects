from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleDeleteView,
    ArticleUpdateView
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    # path('<int:pk>', ArticleDetailView.as_view(), name='article_detail'), # default usage
    path('<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article_update')
]