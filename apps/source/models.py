#_*_ encoding:utf-8 _*_
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager,PermissionsMixin
from django.utils.safestring import mark_safe
# Create your models here.
class Host(models.Model):
    """zhujixinxi"""
    hostname=models.CharField(max_length=80)
    ip_addr=models.GenericIPAddressField(unique=True)
    port = models.PositiveIntegerField(default=22)
    idc = models.ForeignKey("IDC",on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.hostname

    class Meta:
        verbose_name = u"zhujixinxi"
        verbose_name_plural=verbose_name

class IDC(models.Model):
    """zhu ji zu"""
    name = models.CharField(max_length=80,unique=True)

    def __str__(self):
        return self.name


class HostGroup(models.Model):
    """zhu ji zu"""
    name = models.CharField(max_length=80,unique=True)
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name



class UserProfile(AbstractUser):
    """bao lei ji zhang hao"""

class HostUser(models.Model):
    """zhu ji deng lu zhanghao"""
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=180,blank=True,null=True)
    auth_type_choices=((0,"passworld"),(1,"ssh-key"))
    auth_type=models.SmallIntegerField(choices=auth_type_choices,default=0)

    def __str__(self):
        return self.username

    class Meta:
        unique_together=("auth_type","username","password")



class BindHost(models.Model):
    """bang ding zhuji and zhujizhanghao"""
    host= models.ForeignKey("Host",on_delete=models.CASCADE)
    host_user= models.ForeignKey("HostUser",on_delete=models.CASCADE)
    host_group = models.ForeignKey("HostGroup", blank=True, null=True,on_delete=models.CASCADE)
    user = models.ForeignKey("UserProfile",blank=True, null=True,on_delete=models.CASCADE)
    def __str__(self):
        return "%s-%s@%s" %(self.host_group,self.host,self.host_user)

    class Meta:
        unique_together=("host","host_user")