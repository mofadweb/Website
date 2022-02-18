from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView, name="home"),
    path("news", views.Blog.as_view(), name="blog"),
    path("news/search/", views.SearchResults.as_view(), name="blog_search-results"),
    path("news/<slug:slug>", views.PostDetail.as_view(), name="post-detail"),
    path("press-release", views.PressRelease.as_view(), name="press"),
    path(
        "press-release/search/",
        views.PressSearchResults.as_view(),
        name="press_search-results",
    ),
    path("press-release/<slug:slug>", views.PressDetail.as_view(), name="press-detail"),
]
