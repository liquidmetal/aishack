from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

import settings

# Custom modules
from aishack import views

# Uncomment the next two lines to enable the admin
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aishack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
) + static(settings.STATIC_URL)