import django_filters
from .models import Poro
from django_filters import rest_framework as filters


class PoroFilter(filters.FilterSet):

    class Meta:
        model = Poro
        fields = {
            'name': ['contains', 'exact'],
        }