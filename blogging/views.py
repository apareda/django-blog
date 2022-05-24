from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

def list_view_2(request):
    """
    home page view that shows our blog posts
    
    *responsibility is to accept a request and return a response.
    1 - accepts a request and returns a response
    2 - query model and get all the posts that do not have a published date with None
    3 - puts them in reverse published order.
    4 - finds the list.html template.
    5 - injects into the posts
    6 - renders it.
    7 - returns the result as a resonse.
    """

    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    body = template.render(context)

    return HttpResponse(body, content_type="text/html")

def list_view(request):
    """
    home page view that shows our blog posts
    
    *responsibility is to accept a request and return a response.
    1 - accepts a request and returns a response
    2 - query model and get all the posts that do not have a published date with None
    3 - puts them in reverse published order.
    4 - finds the list.html template.
    5 - injects into the posts
    6 - renders it.
    7 - returns the result as a resonse.
    """
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}

    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)