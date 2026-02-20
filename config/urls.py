from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

from config import __version__
from health_check.views import HealthCheckView

admin_header = f"DEFNA v{__version__}"
admin.site.enable_nav_sidebar = False
admin.site.site_header = admin_header
admin.site.site_title = admin_header

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        "health/",
        HealthCheckView.as_view(
            checks=[
                # "health_check.Cache",
                "health_check.Database",
                "health_check.Storage",
            ]
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
