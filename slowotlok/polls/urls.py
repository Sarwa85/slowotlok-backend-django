from django.urls import path

from . import views

urlpatterns = [
    path('card/<int:card_id>', views.get_card, name="get-card")
]