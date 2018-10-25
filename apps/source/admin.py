# from django.contrib import admin
# from .models import *
# # Register your models here.
#
#
# class UserProfileAdmin(admin.ModelAdmin):
#
#     list_display = ['username','password', 'is_staff']
#     search_fields = ['username','password', 'is_staff']
#     list_filter = ['username','password', 'is_staff']
#
# class HostUserAdmin(admin.ModelAdmin):
#     list_display = ['username', 'password', 'auth_type']
#     search_fields = ['username', 'password', 'auth_type']
#     list_filter = ['username', 'password', 'auth_type']
#
# class BindHostAdmin(admin.ModelAdmin):
#     list_display = ['host', 'host_user']
#     search_fields = ['host', 'host_user']
#     list_filter = ['host', 'host_user']
#
# class HostGroupAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     search_fields = ['name']
#     list_filter = ['name', 'bind_hosts']
#
# class IDCAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     search_fields = ['name']
#     list_filter = ['name']
#
#
# class HostAdmin(admin.ModelAdmin):
#     list_display = ['hostname',"ip_addr",'idc']
#     search_fields = ['hostname',"ip_addr",'idc','port']
#     list_filter = ['hostname',"ip_addr",'idc','port','enabled']
#
#
# admin.site.register(Host,HostAdmin)
# admin.site.register(HostUser,HostUserAdmin)
# admin.site.register(UserProfile,UserProfileAdmin)
# admin.site.register(BindHost,BindHostAdmin)
# admin.site.register(IDC,IDCAdmin)
# admin.site.register(HostGroup,HostGroupAdmin)