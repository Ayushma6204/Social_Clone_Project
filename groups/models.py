from django.db import models
from django.utils.text import slugify 
# Create your models here.
import misaka
from django.contrib.auth import get_user_model 
User=get_user_model() 
from django import template 
register=template.Library() 
class Group(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(allow_unicode=True,unique=True)
class GroupMember(models.Model):
    group=models.ForeignKey(Group,related_name='membership')
    user=models.ForeignKey(User,related_name='user_groups')
    def __str__(self):
        return self.user.username 
    class Meta:
        unique_together=('group','user')


    pass 

