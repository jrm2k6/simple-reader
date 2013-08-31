from tastypie.resources import ModelResource
from simplereader_client.models import ReaderUser, Feed

class ReaderUserResource(ModelResource):
    class Meta:
        queryset = ReaderUser.objects.all()
        resource_name = 'ruser'


class FeedResource(ModelResource):
    class Meta:
        queryset = Feed.objects.all()
        resource_name = 'feed'
