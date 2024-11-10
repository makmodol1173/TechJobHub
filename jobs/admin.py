from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Job, Category, Application  # Import the models

# Register the models so they show up in the admin interface
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Application)
