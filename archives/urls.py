from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("about", views.AboutView, name="about"),
    path("contact", views.ContactView, name="contact"),
    path("reports", views.ReportList, name="reports"),
    path("reports/<slug:slug>", views.ReportDetailView.as_view(), name="report-detail"),
    path("agencies", views.Agencies.as_view(), name="agencies"),
    path("agencies/<slug:slug>", views.AgencyDetail.as_view(), name="agency-detail"),
    # Contact View Panel
    path("contact-panel", views.ContactPanel, name="contact-panel"),
    path(
        "contact-panel/login",
        auth_views.LoginView.as_view(template_name="archives/login.html"),
        name="login",
    ),
    path(
        "contact-panel/logout",
        auth_views.LogoutView.as_view(template_name="archives/login.html"),
        name="logout",
    ),
    path(
        "contact-panel/<slug:slug>",
        views.ContactDetailView.as_view(),
        name="contact-detail",
    ),
]
