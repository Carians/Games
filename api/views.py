from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import GameSerializer

# Create your views here.
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    data = request.data
    serializer = GameSerializer
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)