from tastypie.resources import ModelResource
from simplereader_client.models import ReaderUser, Feed
from django.contrib.auth.models import User
from tastypie.authentication import (
    Authentication, ApiKeyAuthentication, BasicAuthentication,
    MultiAuthentication)
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.constants import ALL

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
            'pw': ['exact'],
            'first_name': ['exact']
        }

    def hydrate_pw(self, bundle):
        #bundle.data['pw'] = hashlib.sha1(bundle.data['pw']).hexdigest()
        print 'test'
	return bundle.data['pw']


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
