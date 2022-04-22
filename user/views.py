from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.response import Response


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            user = self.queryset.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"DOES_NOT_EXIST": "User Does not exist"}, status=400)

        queryset = self.queryset.get(id=user.id)
        serializer = self.get_serializer(queryset)
        print(serializer)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(id=request.user.id)
        except ObjectDoesNotExist:
            return Response({"error": "Does not exist"}, status=404)
 
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
