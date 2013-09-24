from tastypie.resources import ModelResource
from simplereader_client.models import ReaderUser, Feed
from django.contrib.auth.models import User
from tastypie.authentication import (
    Authentication, BasicAuthentication,
    SessionAuthentication)
from tastypie.authorization import Authorization
from simplereader_authorization import SimpleReaderAuthorization
from tastypie import fields
from tastypie.constants import ALL
from django.conf.urls import url

import hashlib

class CreateReaderUserResource(ModelResource):
     class Meta:
        allowed_methods = ['post']
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()
        queryset = ReaderUser.objects.all()
        resource_name = 'newuser'


class ReaderUserResource(ModelResource):
    class Meta:
        queryset = ReaderUser.objects.all()
        resource_name = 'user'
        filtering = {
            'email': ['exact'],
            'first_name': ['exact'],
            'last_name': ['exact'],
        }


class MyUserResource(ModelResource):
    class Meta:
        queryset = ReaderUser.objects.all()
        resource_name = 'me'
        list_allowed_methods = ['get']
        authorization = Authorization()
        authentication = SessionAuthentication()
        excludes = ('password', 'id', 'is_active', 'is_admin', 'last_login')

    def get_object_list(self, request): 
        return super(MyUserResource, self).get_object_list(request).filter(pk=request.user.pk)


class FeedResource(ModelResource):
    class Meta:
        queryset = Feed.objects.all()
        resource_name = 'feed'
        filtering = {
            'email_user': ['exact'],
            'category': ['exact'],
            'url': ['exact']
        }


class CreateFeedResource(ModelResource):
    class Meta:
        allowed_methods = ['post']
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()
        queryset = Feed.objects.all()
        resource_name = 'addfeed'
