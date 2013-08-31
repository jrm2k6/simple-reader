from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from simplereader.api import ReaderUserResource, FeedResource

user_resource = ReaderUserResource()
feed_resource = FeedResource()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'simplereader_client.views.home', name='home'),
     url(r'^auth/', 'simplereader_client.views.auth', name='auth'),
     url(r'^api/', include(user_resource.urls)),
     url(r'^api/', include(feed_resource.urls)),
    # url(r'^simplereader/', include('simplereader.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
