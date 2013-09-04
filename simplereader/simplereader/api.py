from tastypie.resources import ModelResource
from simplereader_client.models import ReaderUser, Feed
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from tastypie.authentication import (
    Authentication, ApiKeyAuthentication, BasicAuthentication,
    MultiAuthentication)
from tastypie.authorization import Authorization
from tastypie import fields


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
        allowed_methods = ['get, put, patch']
        resource_name = 'user'


class FeedResource(ModelResource):
    class Meta:
        queryset = Feed.objects.all()
        resource_name = 'feed'


class CreateFeedResource(ModelResource):
    class Meta:
        allowed_methods = ['post']
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()
        queryset = Feed.objects.all()
        resource_name = 'addfeed'
