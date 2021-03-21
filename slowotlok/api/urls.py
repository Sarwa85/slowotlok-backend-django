from django.urls import path
from .cardlistview import CardListView
from .cardview import CardView

urlpatterns = [
    path("card/", CardListView.as_view()),
    path('card/<int:card_id>', CardView.as_view()),

    # path('score/add', controler.score_add, name="score-add")
]