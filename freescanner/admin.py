from django.contrib import admin
from .models import Identifiers


class IdentifiersAdmin(admin.ModelAdmin):
    list_display = (
        'identifier_name',
        'identifier_id',
        'identifier_type',
        'identifier_comment',
    )

    ordering = ('identifier_name',)


admin.site.register(Identifiers, IdentifiersAdmin)
