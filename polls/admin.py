from django.contrib import admin
from .models import TeacherModel
from .forms import TeacherForm
# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    form=TeacherForm
    list_display=('name',)
    search_fields=('name',)

admin.site.register(TeacherModel,TeacherAdmin)