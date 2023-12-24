from django.urls import path, include
from .views import PoroCreationFormView, PoroListView, PoroApiView

forms = [
    path('create/', PoroCreationFormView.as_view()),
]

api = [
    path('', PoroApiView.as_view()),
    path('list/', PoroListView.as_view()),
]

urlpatterns = [
    path('api/v1/poro/', include(api)),
    path('forms/v1/poro/', include(forms))
]