from rest_framework import generics, permissions, mixins, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.portfolio.models import Portfolio, Photos, Comments
from apps.portfolio.serializers import PortfolioSerializer, PhotosSerializer, CommentsSerializer


class PortfolioView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                    mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    model = Portfolio
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PhotosView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                 mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    model = Photos
    serializer_class = PhotosSerializer

    def get_queryset(self):
        return Photos.objects.all()


class CommentsView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    model = Comments
    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comments.objects.all()

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)

