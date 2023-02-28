from django.contrib import admin
from .models import Member
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_dispaly = ("firstname", "lastname", "id",)

admin.site.register(Member,MemberAdmin)