from django.db import models

class ScrapingSandbox(models.Model):
    name = models.CharField(max_length=50)
    source_url = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    scraped_on = models.DateField(auto_now=True)

    class Meta:
        unique_together = ('source_url', 'scraped_on',)
