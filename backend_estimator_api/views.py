from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics
from backend_estimator_api.estimator import estimator
from backend_estimator_api.serializers import LogSerializer
from backend_estimator_api.models import Log


class Estimator(APIView):
    """
    Class view to return response from estimator module.
    """

    def post(self, request):
        """
        Return data as well as impact and severe impact estimations.
        """
        data = request.data
        res = estimator(data)
        return Response(res, status=status.HTTP_200_OK)


class LogViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Log.objects.all()
    serializer_class = LogSerializer
