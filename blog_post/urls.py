from django.urls import path
from .views import BlogPostView, BlogDetailView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogPostView.as_view(), name='home')
]
