from rest_framework import viewsets, filters
from .models import CustomUser
from .Serializer import UserSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id','email')



