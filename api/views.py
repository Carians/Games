from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import json

# Create your views here.
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    return Response({
        'supported_apis_urls': {
        'games': reverse('main:games', request=request),
        'gamesreviews': reverse('main:gamesreview', request=request),
        }
    })