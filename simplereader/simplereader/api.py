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
    user = fields.OneToOneField('UserResource', 'user', full=False)
    
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
        resource_name = 'ruser'


class UserResource(ModelResource):
    raw_password = fields.CharField(attribute=None, readonly=True, null=True,
                                    blank=True)
 
    class Meta:
        authentication = MultiAuthentication(
            BasicAuthentication(),
            ApiKeyAuthentication())
        authorization = Authorization()
 
        allowed_methods = ['get', 'patch', 'put', ]
        always_return_data = True
        queryset = User.objects.all().select_related("api_key")


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
