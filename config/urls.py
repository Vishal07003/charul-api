from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path("", RedirectView.as_view(url="panel/", permanent=False)),

    path("admin/", admin.site.urls),

    path("panel/", include("apps.panel.urls")),

    path("api/projects/", include("apps.projects.urls")),
    path("api/categories/", include("apps.categories.urls")),
    path("api/services/", include("apps.services.urls")),
    path("api/home/", include("apps.home.urls")),
    path("api/reviews/", include("apps.reviews.urls")),
    path("api/contact/", include("apps.contact.urls")),
    path("api/practice/", include("apps.practice.urls")),
    path("api/stats/", include("apps.stats.urls")),
    path("api/process/", include("apps.process.urls")),

    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]