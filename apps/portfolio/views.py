from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, mixins, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.portfolio.models import Portfolio, Photo, Comments
from apps.portfolio.serializers import PortfolioSerializer, PhotoSerializer, CommentsSerializer


class PortfolioView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                    mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    model = Portfolio
    serializer_class = PortfolioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PhotoView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                 mixins.DestroyModelMixin, mixins.UpdateModelMixin, viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    model = Photo
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'portfolio__name']

    def get_queryset(self):
        return Photo.objects.all()


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

