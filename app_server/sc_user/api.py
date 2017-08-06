
from rest_framework import routers, serializers, viewsets
from models import UserInfo
from serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer