from django.db import models
from django.utils.html import format_html


class ScrapingSandbox(models.Model):
    name = models.CharField(max_length=100)
    source_url = models.URLField(max_length=100)
    description = models.TextField(max_length=500)
    scraped_on = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('source_url', 'scraped_on',)
        verbose_name = 'Scraping Sandbox'
        verbose_name_plural = 'Scraping Sandboxes'
        get_latest_by = 'scraped_on'

    def source_link(self):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=self.source_url)
