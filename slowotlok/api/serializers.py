from rest_framework import serializers

from .models import Card, Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["good", "bad"]


class CardSerializer(serializers.ModelSerializer):
    score = ScoreSerializer()

    class Meta:
        model = Card
        fields = ["id", "source", "tr", "score"]


class CardRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ["source", "tr"]
