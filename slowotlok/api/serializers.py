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
        s_data = validated_data.pop('score')
        validated_data['score'] = ScoreSerializer.create(ScoreSerializer(), validated_data=s_data)
        c, created = Card.objects.update_or_create(**validated_data)
        return c

