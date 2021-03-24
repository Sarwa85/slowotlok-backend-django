from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Card
from .serializers import CardSerializer


class CardView(APIView):
    http_method_names = ['get', 'delete', 'patch']

    def delete(self, request, card_id, *args, **kwargs):
        c = Card.objects.get(id=card_id)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, card_id, *args, **kwargs):
        c = Card.objects.get(id=card_id)
        return Response(CardSerializer(c).data, status=200)

    def patch(self, request, card_id, *args, **kwargs):
        d = request.data
        if CardSerializer(data=d).is_valid():
            s = d.pop("score")
            card = Card.objects.get(pk=card_id)
            card.__dict__.update(d)
            score = card.score
            score.__dict__.update(s)
            score.save()
            card.save()
            return Response(CardSerializer(card).data, status=status.HTTP_200_OK)
        return Response("asd", status=status.HTTP_400_BAD_REQUEST)