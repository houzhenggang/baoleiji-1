# from django.contrib import admin
from .models import *
# Register your models here.
import xadmin

class UserProfileAdmin(object):

    list_display = ['username','password', 'is_staff']
    search_fields = ['username','password', 'is_staff']
    list_filter = ['username','password', 'is_staff']

class HostUserAdmin(object):
    list_display = ['username', 'password', 'auth_type']
    search_fields = ['username', 'password', 'auth_type']
    list_filter = ['username', 'password', 'auth_type']

class BindHostAdmin(object):
    list_display = ['host_group','host', 'host_user']
    search_fields = ['host_group', 'host_user']
    list_filter = ['host_group', 'host_user']

class HostGroupAdmin(object):
    list_display = ['name','user']
    search_fields = ['name','user']
    list_filter = ['name','user']

class IDCAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class HostAdmin(object):
    list_display = ['hostname',"ip_addr",'idc']
    search_fields = ['hostname',"ip_addr",'idc','port']
    list_filter = ['hostname',"ip_addr",'idc','port','enabled']


xadmin.site.register(Host, HostAdmin)
xadmin.site.register(HostUser, HostUserAdmin)
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(BindHost, BindHostAdmin)
xadmin.site.register(IDC, IDCAdmin)
xadmin.site.register(HostGroup, HostGroupAdmin)