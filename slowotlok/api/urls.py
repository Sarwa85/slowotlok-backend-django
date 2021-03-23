from django.urls import path
from .cardlistview import CardListView
from .cardview import CardView

urlpatterns = [
    # get, post
    path("cards", CardListView.as_view(), name="card"),

    # get, delete
    path('cards/<int:card_id>', CardView.as_view(), name="card_with_id"),
]
