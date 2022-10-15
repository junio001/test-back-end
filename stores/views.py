from stores.models import Store
from stores.serializer import StoreSerializer
from rest_framework import generics


class StoreView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
