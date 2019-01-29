from rest_framework.generics import ListAPIView

from .serializers import ListSerializers, CardSerializers
from .models import List, Card

class ListApi(ListAPIView):
    # where to get the data
    queryset = List.objects.all()
    # how to convert it to json
    serializer_class = ListSerializers

class CardApi(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers