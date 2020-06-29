from django.contrib import admin
from App_TestModel.models import Test, Contact, Tag

# Register your models here.
admin.site.register([Test, Contact, Tag])