from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Card
from .serializers import CardSerializer


class CardView(APIView):
    http_method_names = ['get', 'post', 'put', 'delete']

    def delete(self, request, card_id, *args, **kwargs):
        c = Card.objects.get(id=card_id)
        c.delete()
        return Response(CardSerializer(c).data, status=200)

    def get(self, request, card_id, *args, **kwargs):
        c = Card.objects.get(id=card_id)
        return Response(CardSerializer(c).data, status=200)
