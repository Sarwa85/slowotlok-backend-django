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

    # def to_representation(self, obj):
    #     """Move fields from profile to user representation."""
    #     representation = super().to_representation(obj)
    #     score_representation = representation.pop('score')
    #     for key in score_representation:
    #         representation[key] = score_representation[key]
    #     return representation
