from rest_framework import serializers

from .models import Card, Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["good", "bad"]


class CardSerializer(serializers.ModelSerializer):
    score = ScoreSerializer(required=True)

    class Meta:
        model = Card
        fields = ["id", "source", "tr", "score"]

    def create(self, validated_data):
        score_data = validated_data.pop('score')
        validated_data["score"] = Score.objects.create(**score_data)
        return Card.objects.create(**validated_data)
