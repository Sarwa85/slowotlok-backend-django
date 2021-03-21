from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Card
from .serializers import CardSerializer


class CardListView(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        c = Card.objects.all()
        return Response(CardSerializer(c, many=True).data, status=200)
