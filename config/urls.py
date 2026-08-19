from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/projects/", include("apps.projects.urls")),
    path("api/categories/", include("apps.categories.urls")),
    path("api/services/", include("apps.services.urls")),
    path("api/home/", include("apps.home.urls")),
    path("api/reviews/", include("apps.reviews.urls")),
    path("api/contact/", include("apps.contact.urls")),
    path("api/practice/", include("apps.practice.urls")),
    path("api/stats/", include("apps.stats.urls")),
    path("api/process/", include("apps.process.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)