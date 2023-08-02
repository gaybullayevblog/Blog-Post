# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post
# Create your views here.

class BlogPostView(ListView):
    model = Post
    template_name = 'home.html'


class React(ListView):
    model = Post
    template_name = 'pages/react.html'


class About(ListView):
    model = Post
    template_name = 'pages/about.html'


class Javascript(ListView):
    model = Post
    template_name = 'pages/javascript.html'


class Python(ListView):
    model = Post
    template_name = 'pages/python.html'


class Vue(ListView):
    model = Post
    template_name = 'pages/vue.html'


class TelegramBot(ListView):
    model = Post
    template_name = 'pages/telegrambot.html'


class Django(ListView):
    model = Post
    template_name = 'pages/django.html'



class Linux(ListView):
    model = Post
    template_name = 'pages/linux.html'



class Tailwindcss(ListView):
    model = Post
    template_name = 'pages/tailwindcss.html'


class Bootstrap(ListView):
    model = Post
    template_name = 'pages/bootstrap.html'


class Portfolio(ListView):
    model = Post
    template_name = 'pages/portfolio.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')