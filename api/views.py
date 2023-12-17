from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData (request):
    items=Item.objects.all()
    serializer=ItemSerializer(items,many=True) #serializing the data
    return Response(serializer.data)

@api_view(['POST'])
def addItems (request):
    serializer=ItemSerializer(data=request.data) #getting the data from the request
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)