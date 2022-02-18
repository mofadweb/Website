from django.shortcuts import render
from django.views import generic
from .models import Post
from leadership.models import Leader
from events.models import Event

from django.db.models import Q


def HomeView(request):
    post_list = Post.objects.filter(type="Blog")[:6]
    event_list = Event.objects.all()[:6]
    leader_list = Leader.objects.filter(feature=True)[:3]
    context = {"posts": post_list, "events": event_list, "leaders": leader_list}
    return render(request, "home.html", context)


class Blog(generic.ListView):
    model = Post
    template_name = "blog/blog.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(type="Blog")
        context["posts_count"] = Post.objects.filter(type="Blog").count()
        return context


class SearchResults(generic.ListView):
    model = Post
    template_name = "blog/blog_search.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super(SearchResults, self).get_context_data(**kwargs)
        query = self.request.GET.get("q")
        context["results"] = Post.objects.filter(Q(type="Blog", title__icontains=query))
        return context


class PostDetail(generic.View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(type="Blog", slug=self.kwargs["slug"])
        other_posts = Post.objects.exclude(type="Blog", slug=self.kwargs["slug"])[:3]

        context = {"post": post, "other_posts": other_posts}

        return render(request, "blog/post_detail.html", context=context)


class PressRelease(generic.ListView):
    model = Post
    template_name = "blog/press.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(PressRelease, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(type="Press release")
        context["posts_count"] = Post.objects.filter(type="Press release").count()
        return context


class PressSearchResults(generic.ListView):
    model = Post
    template_name = "blog/press_search.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super(PressSearchResults, self).get_context_data(**kwargs)
        query = self.request.GET.get("q")
        context["results"] = Post.objects.filter(
            Q(type="Press release", title__icontains=query)
        )
        return context


class PressDetail(generic.View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(type="Press release", slug=self.kwargs["slug"])
        other_posts = Post.objects.exclude(
            type="Press release", slug=self.kwargs["slug"]
        )[:3]

        context = {"post": post, "other_posts": other_posts}

        return render(request, "blog/press_detail.html", context=context)
