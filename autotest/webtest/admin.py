from django.contrib import admin
from webtest.models import WebCase,WebCaseStep

# Register your models here.


class WebCaseStepAdmin(admin.TabularInline):
    list_display = ['webcasename','webteststep','webtestobjname','webfindmethod','webevelement','weboptmethod','webassertdata','webtestresult','create_time','id','webcase']
    model = WebCaseStep
    extra = 1


class WebCaseAdmin(admin.ModelAdmin):
    list_display = ['webcasename','webtestresult','create_time','id']
    inlines = [WebCaseStepAdmin]


admin.site.register(WebCase,WebCaseAdmin)
