from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Card, Score
from .serializers import CardSerializer, CardRequestSerializer


class CardListView(APIView):
    http_method_names = ['get', 'post']

    def get(self, request: Request, *args, **kwargs):
        c = Card.objects.all()
        return Response(CardSerializer(c, many=True).data, status=status.HTTP_200_OK)

    def post(self, request: Request, *args, **kwargs):
        card_request = CardRequestSerializer(data=request.data)

        if card_request.is_valid():
            score = Score(bad=0, good=0)
            card = Card(source=card_request.data['source'], tr=card_request.data['tr'], score=score)
            score.save()
            card.save()
            return Response(CardSerializer(card).data, status=status.HTTP_201_CREATED)
        return Response(card_request.errors, status=status.HTTP_400_BAD_REQUEST)
