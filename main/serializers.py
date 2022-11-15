from rest_framework import serializers
from .models import Games

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        # fields = [
        #     "title",
        #     "description",
        #     "text",
        #     "date_created",
        #     "link",
        #     "imgURL"
        # ]
        fields = '__all__'