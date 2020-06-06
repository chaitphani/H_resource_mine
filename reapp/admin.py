from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django import forms
from import_export.admin import ImportExportModelAdmin

# Register your models here.


app_models = apps.get_app_config('reapp').get_models()
for model in app_models:
    try:
        @admin.register(model)
        # admin.site.register(model)
        class ModelAdmin(ImportExportModelAdmin):
            pass
    except AlreadyRegistered:
        pass