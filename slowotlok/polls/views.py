from django.http import HttpResponse
from .models import Card


def get_card(request, card_id):
    c = Card.objects.get(id=card_id)
    return HttpResponse(c, status=200)
