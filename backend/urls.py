from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from backend_estimator_api.views import Estimator, LogViewSet


urlpatterns = [
    path('api/v1/on-covid-19/', Estimator.as_view()),
    path('api/v1/on-covid-19/logs/', LogViewSet.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
