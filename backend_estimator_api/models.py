from django.db import models


class Log(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    http_method = models.CharField(max_length=10)
    request_path = models.CharField(max_length=50)
    request_status = models.CharField(max_length=20)
    request_time = models.CharField(max_length=10)
