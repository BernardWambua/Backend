import datetime
from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from backend_estimator_api.serializers import LogSerializer
from backend_estimator_api.models import Log as LogModel
from dicttoxml import dicttoxml
from backend_estimator_api.estimator import estimator


def get_time_diff(start, end):
    delta = end - start
    return delta.total_seconds() * 1000


class Estimator(APIView):
    """
        Estimator APIView
    """

    def _save_log(self, log):
        serializer = LogSerializer(data=log)
        if serializer.is_valid():
            serializer.save()

    def post(self, request, res_fmt='json'):
        """
        Return a list of all users.
        """
        start = datetime.datetime.now()
        log = {
            'endpoint': self.request.META['PATH_INFO'],
            'method': self.request.META['REQUEST_METHOD'],
        }
        data = request.data
        res = estimator(data)
        if res_fmt == 'xml':
            end = datetime.datetime.now()
            log['status'] = '200'
            log['response_time'] = f"{str(get_time_diff(start, end))} ms"
            self._save_log(log)
            return Response(dicttoxml(res), status=status.HTTP_200_OK, content_type='application/xml')
        else:
            end = datetime.datetime.now()
            log['status'] = '200'
            log['response_time'] = f"{str(get_time_diff(start, end))} ms"
            self._save_log(log)
            return Response(res, status=status.HTTP_200_OK)


class Log(APIView):
    """ Logs Viewset"""

    def _save_log(self, log):
        serializer = LogSerializer(data=log)
        if serializer.is_valid():
            serializer.save()

    def get(self, request):
        start = datetime.datetime.now()
        log = {
            'request_path': self.request.META['PATH_INFO'],
            'http_method': self.request.META['REQUEST_METHOD'],
        }
        logs = LogModel.objects.all()
        serializer = LogSerializer(logs, many=True)
        end = datetime.datetime.now()
        log['request_status'] = '200'
        log['request_status'] = f"{str(get_time_diff(start, end))} ms"
        self._save_log(log)
        res = [f"{res['http_method']}    {res['request_path']}   {res['request_status']}     {res['request_status']}"
               for res in serializer.data]
        return Response(res, status=status.HTTP_200_OK)
