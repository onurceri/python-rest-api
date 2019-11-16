from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)

from core.serializers import UserSerializer


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.create(serialized.validated_data)
        return Response(serialized.data, status=HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=HTTP_400_BAD_REQUEST)
