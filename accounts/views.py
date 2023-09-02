from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .permissions import UserPermissions
from .models import User

# Create your views here.
class UserApiView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(instance=user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request):
        user = request.user
        serializer = UserSerializer(data=request.data, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)