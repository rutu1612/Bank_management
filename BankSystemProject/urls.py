from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name = "home"),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^profile/', include("profiles.urls")),
    url(r'^admins/', include("admins.urls")),
    url(r'^send/', views.sms),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
