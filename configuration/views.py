from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Country, Language, Religion
from .serializers import CountrySerializer, LanguageSerializer, ReligionSerializer


class ConfigurationViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]

    @action(methods=['GET', ], detail=False, url_path='all-countries')
    def get_all_countries(self, request):
        countries = Country.objects.all().order_by('country')
        data = {'countries': CountrySerializer(countries, many=True).data}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['GET', ], detail=False, url_path='all-languages')
    def get_all_languages(self, request):
        languages = Language.objects.all().order_by('language')
        data = {'languages': LanguageSerializer(languages, many=True).data}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['GET', ], detail=False, url_path='all-religions')
    def get_all_religions(self, request):
        religions = Religion.objects.all().order_by('religion')
        data = {'religions': ReligionSerializer(religions, many=True).data}
        return Response(data=data, status=status.HTTP_200_OK)

