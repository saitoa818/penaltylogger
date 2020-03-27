from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event
from .models import Log
from .models import Judge
from .models import Penalty
from .models import Violation

class JudgeAdmin(UserAdmin):
    model = Judge
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('judge_id',)}),)
    list_display = ['username', 'password', 'judge_id']

admin.site.register(Judge, JudgeAdmin)
admin.site.register(Event)
admin.site.register(Log)
#admin.site.register(Judge)
admin.site.register(Penalty)
admin.site.register(Violation)