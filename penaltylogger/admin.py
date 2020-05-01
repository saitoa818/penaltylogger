from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event
from .models import Log
from .models import Penalty
from .models import Violation
from .models import Judge
from django.contrib.auth.models import Group, User

from django.contrib.auth.forms import UserChangeForm
###

from django import forms
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    judge_id = forms.CharField(label='judge_id')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Judge
        fields = ('judge_id', 'password')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = Judge
        fields = '__all__'


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('judge_id', 'is_staff', 'log_view')
    list_filter = ('judge_id', 'groups')
    fieldsets = (
        (None, {'fields': ('judge_id', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'log_view', )}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'judge_id', 'password'
            ),
        }),
    )
    search_fields = ('judge_id',)
    ordering = ('judge_id',)
    filter_horizontal = ()

###

class JudgeAdmin(UserAdmin):
    model = Judge
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('judge_id',)}),)
    list_display = ['password', 'judge_id', 'is_staff']

admin.site.register(Judge, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Event)
admin.site.register(Log)
admin.site.register(Penalty)
admin.site.register(Violation)

