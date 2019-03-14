from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Election)
admin.site.register(models.Posts)
admin.site.register(models.VoterTypes)
admin.site.register(models.VoterLists)