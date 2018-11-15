from django.contrib import admin
from properties.models import Prop
from django.utils.html import format_html

class PropAdmin(admin.ModelAdmin):
    """
    Property admin page.
    """
    save_on_top = True
    list_display = ('id', 'view', 'created_at', 'updated_at')
    search_fields = ()
    list_filter = () 

    def view(self, obj):
        """
        Return a link.
        """
        return format_html('<a href="%s" target=_blank>%s</a>' % (obj.link, obj.zillow_id))
    view.allow_tags = True

admin.site.register(Prop, PropAdmin)