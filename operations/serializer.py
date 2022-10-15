from rest_framework import serializers
from stores.serializer import StoreSerializer
from operations.models import Operation

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"
    


class OperationStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"
    
    store = StoreSerializer(read_only=True)

