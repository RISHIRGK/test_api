from . import models
from rest_framework import serializers


from . import models

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = models.book
        fields = "__all__"
