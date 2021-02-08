from django.contrib import admin
from .models import Blogs
# Register your models here.
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_on')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True

admin.site.register(Blogs)
