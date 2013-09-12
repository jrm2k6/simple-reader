from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from simplereader.api import (
    ReaderUserResource, FeedResource, 
    CreateReaderUserResource, CreateFeedResource)

user_resource = ReaderUserResource()
create_user_resource = CreateReaderUserResource()
feed_resource = FeedResource()
create_feed_resource = CreateFeedResource()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'simplereader_client.views.home', name='home'),
     url(r'^auth/', 'simplereader_client.views.auth', name='auth'),
     url(r'^signup/', 'simplereader_client.views.signup', name='signup'),
     url(r'^signin/', 'simplereader_client.views.signin', name='signin'),
     url(r'^api/', include(user_resource.urls)),
     url(r'^api/', include(create_user_resource.urls)),
     url(r'^api/', include(feed_resource.urls)),
     url(r'^api/', include(create_feed_resource.urls)),
    # url(r'^simplereader/', include('simplereader.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
