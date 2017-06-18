"""xyz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from team.views import TeamView
from home.views import HomeView
from stories.views import StoriesView
from contact.views import ContactView
from django.views.decorators.cache import cache_page


urlpatterns = [
    url(r'^$', cache_page(60 * 15)(HomeView.as_view())),
    url(r'^team/', cache_page(60 * 15)(TeamView.as_view())),
    url(r'^stories/', cache_page(60 * 15)(StoriesView.as_view())),
    url(r'^contact/', cache_page(60 * 15)(ContactView.as_view())),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
