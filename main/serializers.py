from rest_framework import serializers
from django.db.models import Avg
from .models import Games, GamesReview
#from  api.serializers import UserPublicSerializer

class GameReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = GamesReview
        fields = '__all__'


class GameReviewInLineSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='gamesreview-detail',
        lookup_field='owner',
        read_only=True
    )

class GameSerializer(serializers.ModelSerializer):
    review_ratio = serializers.SerializerMethodField(read_only=True)

    #user_rate = GameReviewInLineSerializer( read_only=True,many=True)

    class Meta:

        model = Games
        fields = [
            "title",
            "description",
            "text",
            #"user_rate",
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