from django.contrib import admin
from .models import Doc
from .forms import DocumentForm
admin.autodiscover()

class xyz(admin.ModelAdmin):
    form =DocumentForm
    model = Doc
    list_display=['description']
    search_fields = ['=description']
    list_filter= ['description']
admin.site.register(Doc, xyz)
# Register your models here.
