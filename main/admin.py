from django.contrib import admin
from .models import Home

# Register your models here.
admin.site.site_header = 'Business Admin Panel'
class IndexAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Home, IndexAdmin)
