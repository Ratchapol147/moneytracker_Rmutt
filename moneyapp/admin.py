from django.contrib import admin
from moneyapp.models import Statement



class StatementAdmin(admin.ModelAdmin):
    list_display=['name','amount','category']  #สร้างตาราง


admin.site.register(Statement,StatementAdmin)


