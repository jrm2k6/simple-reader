from tastypie.authorization import Authorization

class SimpleReaderAuthorization(Authorization):
	def read_list(self, object_list, bundle):
		return object_list.filter(email=bundle.request.user.email)