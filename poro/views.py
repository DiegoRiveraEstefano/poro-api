from django.views.generic import FormView
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.request import Request
from rest_framework.response import Response
import serial

from .forms import PoroCreationForm, PoroEditForm, PoroDeleteForm
from .pagination import StandardResultsSetPagination
from .serializer import PoroSerializer
from .models import Poro
from .filters import PoroFilter


# forms views
class PoroCreationFormView(FormView):
    template_name = "components/forms/poro/creation.html"
    form_class = PoroCreationForm
    success_url = "/api/v1/poro/"


# api views
class PoroListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = PoroSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    pagination_class = StandardResultsSetPagination
    filterset_class = PoroFilter

    def get_queryset(self):
        user = self.request.user
        return Poro.objects.filter(owner=user)


class PoroApiView(generics.CreateAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PoroSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        user = self.request.user
        return Poro.objects.filter(owner=user)

    def create(self, request, *args, **kwargs):

        # todo: check if a poro exist with this name
        print(request.data)
        new_poro = Poro(**{
            'owner': self.request.user,
            'UUID': self.request.data['UUID'],
            'name': self.request.data['name']
        })
        new_poro.save()
        print(new_poro)
        return Response(201)

    def update(self, request, *args, **kwargs):
        poro = Poro.objects.filter(UUID=request.data['UUID'], owner=self.request.user)
        if not poro:
            return Response(404)
        return Response(201)

    def delete(self, request, *args, **kwargs):
        poro = Poro.objects.filter(UUID=request.data['UUID'], owner=self.request.user)
        if not poro:
            return Response(404)
        poro.delete()
        return Response(201)


