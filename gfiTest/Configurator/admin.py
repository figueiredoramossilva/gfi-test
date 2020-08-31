# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.forms import TextInput, Textarea
from django.db import models

from django_mptt_admin.admin import DjangoMpttAdmin

from zipfile import ZipFile
from django.http import HttpResponse

from .models import Customer
from .models import Equipment



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ip', 'hostname', 'address', 'created_at', 'updated_at')
    
    list_display_links = ('id', 'name', 'ip', 'hostname', 'address', 'created_at', 'updated_at')
    
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'31'})},
        models.GenericIPAddressField: {'widget': TextInput(attrs={'size':'31'})}
    }

    def download_configurator(modeladmin, request, queryset, zip_files=False):

        # create zip if > 1
        # set the flag for zipping the files
        if (len(queryset) > 1):
            zipObj = ZipFile('configurations.zip', 'w')
            zip_files = True

        for s in queryset:
            layout = s.get_layout().encode('ascii', 'ignore')
            layout = layout.replace("{{ IP }}", s.ip)
            layout = layout.replace("{{ HOSTNAME }}", s.hostname)
            layout = layout.replace("{{ CLIENT_NAME }}", s.name)
            layout = layout.replace("{{ MORADA }}", s.address)

            filename = s.name + ".txt"
            with open(filename, 'wb') as f:
                f.write(layout)

            # return just the file
            if (not zip_files):
                df = open(filename, 'r')
                response = HttpResponse(df, content_type='text/txt')
                response['Content-Disposition'] = 'attachment; filename=' + filename
                return response

            # move to zip file
            zipObj.write(filename)

        zipObj.close()

        response = HttpResponse(zipObj, content_type='application/x-zip-compressed')
        response['Content-Disposition'] = 'attachment; filename=' + zipObj.filename
        return response
        

            
        

    download_configurator.short_description = "Download Configurator"

    actions = ['download_configurator']



class EquipmentAdmin(DjangoMpttAdmin):
    pass



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Equipment, EquipmentAdmin)


