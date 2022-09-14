from django.contrib.auth.models import User
from rest_framework import generics, status, permissions, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.serializers import UserSerializer, RegisterSerializer


class LoginView(TokenObtainPairView):
    permission_classes = ()
    authentication_classes = ()


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'You are logged out'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.GenericAPIView, mixins.CreateModelMixin, viewsets.ViewSet):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = RegisterSerializer


class UserView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
               mixins.UpdateModelMixin, viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    model = User
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)
