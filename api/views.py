import os
from datetime import date, timedelta
from scraper.apps import SpiderController
from scraper.models import ScrapingSandbox
from api.serializers import ScrapingSandboxSerializer
from rest_framework import viewsets, permissions, renderers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from scraper.scraper.spiders.scrapethissite import ScrapethissiteSpider


class ScrapingSandboxViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScrapingSandbox.objects.all().order_by('-scraped_on')
    serializer_class = ScrapingSandboxSerializer

    @action(detail=False)
    def new(self, request, *args, **kwargs):
        most_recent = self.queryset.latest().scraped_on

        if most_recent > date.today() - timedelta(days=7):
            serializer = self.serializer_class(self.queryset.filter(scraped_on=most_recent), many=True)
            return Response(serializer.data)

        SpiderController.run_spider('scrapethissite', signal=False)

        serializer = self.serializer_class(self.queryset.filter(scraped_on=date.today()), many=True)
        return Response(serializer.data)


class SandboxRecent(APIView):
    def get(self, request):
        queryset = ScrapingSandbox.objects.all().order_by('-scraped_on')
        serializer = ScrapingSandboxSerializer(queryset, many=True)
        return Response(serializer.data)
