from django.contrib import admin
from .models import Log
from .models import Penalty
from .models import Violation

admin.site.register(Log)
admin.site.register(Penalty)
admin.site.register(Violation)