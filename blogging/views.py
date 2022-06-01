from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
