from django.urls import path

from . import views

app_name = "panel"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.dashboard, name="dashboard"),
    path("contact/", views.contact_edit, name="contact_edit"),
    path("<slug:key>/", views.resource_list, name="resource_list"),
    path("<slug:key>/new/", views.resource_create, name="resource_create"),
    path("<slug:key>/<int:pk>/edit/", views.resource_edit, name="resource_edit"),
    path("<slug:key>/<int:pk>/delete/", views.resource_delete, name="resource_delete"),
]
