from rest_framework import generics, status
from django.contrib.auth.models import User
# from rest_framework import viewsets
from users.api.serializers import RegisterSerializer


# class RegiterView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
