from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from simplereader_client.models import Feed, ReaderUser


class ReaderUserInline(admin.StackedInline):
    model = ReaderUser
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = (ReaderUserInline, )

admin.site.register(Feed)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)