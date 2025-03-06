from django.contrib import admin
from .models import Topic, Comment

# Register models
admin.site.register(Topic)
admin.site.register(Comment)
