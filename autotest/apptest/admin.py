from django.contrib import admin
from apptest.models import AppCase,AppCaseStep

# Register your models here.


class AppCaseStepAdmin(admin.TabularInline):
    list_display = ['appteststep','apptestobjname','appfindmethod','appevelement','appoptmethod','appassertdata','apptestresult','create_time','id','appcase']
    model = AppCaseStep
    extra = 1


class AppCaseAdmin(admin.ModelAdmin):
    list_display = ['appcasename','apptestresult','create_time','id']
    inlines = [AppCaseStepAdmin]


admin.site.register(AppCase,AppCaseAdmin)