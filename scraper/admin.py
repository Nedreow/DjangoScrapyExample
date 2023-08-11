from django.contrib import admin
from scraper.models import ScrapingSandbox


class ScrapingSandboxAdmin(admin.ModelAdmin):
    list_display = ('name', 'source_link', 'scraped_on')
    readonly_fields = ('source_url', 'scraped_on')


admin.site.register(ScrapingSandbox, ScrapingSandboxAdmin)
