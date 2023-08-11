from scraper.models import ScrapingSandbox
from rest_framework import serializers

class ScrapingSandboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapingSandbox
        fields = ['name', 'description', 'source_url', 'scraped_on']
