from django.contrib import admin
from .models import *
from django.forms import ModelForm, ValidationError


class ApplyAdminForm(ModelForm):
    class Meta:
        model = Apply
        exclude = []

        def clean_account(self):
            account = self.data['account']
            app_status = self.data['application_status']
            if app_status != 'Account Opening' and account == null:
                raise ValidationError('Create an account number since account status has changed')

            return account

class ApplyAdmin(admin.ModelAdmin):
    form = ApplyAdminForm


admin.site.register(Apply, ApplyAdmin)
admin.site.register(Account)
