from django.contrib import admin
from .models import Event
from .models import Log
from .models import Judge
from .models import Penalty
from .models import Violation

admin.site.register(Event)
admin.site.register(Log)
admin.site.register(Judge)
admin.site.register(Penalty)
admin.site.register(Violation)