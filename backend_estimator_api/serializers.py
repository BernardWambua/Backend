from rest_framework import serializers
from .models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['http_method', 'request_path',
                  'request_status', 'request_time']
