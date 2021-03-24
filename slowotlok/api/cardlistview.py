from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Card, Score
from .serializers import CardSerializer


class CardListView(APIView):
    http_method_names = ['get', 'post']

    def get(self, request: Request):
        c = Card.objects.all()
        return Response(CardSerializer(c, many=True).data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        card_serializer = CardSerializer(data=request.data)
        if card_serializer.is_valid(raise_exception=True):
            c = card_serializer.create(validated_data=request.data)
            return Response(CardSerializer(c).data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
