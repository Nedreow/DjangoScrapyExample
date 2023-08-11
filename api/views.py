from django.shortcuts import render
from scraper.models import ScrapingSandbox
from rest_framework import viewsets, permissions
from api.serializers import ScrapingSandboxSerializer

class ScrapingSandboxViewSet(viewsets.ModelViewSet):
    queryset = ScrapingSandbox.objects.all().order_by('-scraped_on')
    serializer_class = ScrapingSandboxSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

