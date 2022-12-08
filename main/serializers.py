from rest_framework import serializers
from django.db.models import Avg
from .models import Games, GamesReview

class GameReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = GamesReview
        fields = [
            'owner',
            'gameName',
            'rate',
            'date_created'
        ]

class GameReviewHyperlink(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GamesReview
        fields= '__all__'

class GameSerializer(serializers.ModelSerializer):
    review_ratio = serializers.SerializerMethodField(read_only=True)
    user_rate = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='gamesreview-detail:main',
    )

    class Meta:

        model = Games
        fields = [
            "title",
            "description",
            "text",
            "user_rate",
            "date_created",
            "review_ratio",
            "link",
            "imgURL"
        ]

    def get_review_ratio(self, instance):
        return GamesReview.objects.all().filter(gameName=instance.pk).aggregate(Avg('rate'))['rate__avg']


class GamePUTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = [
            "title",
            "text",
            "description",
            "date_created",
            "imgURL"
        ]