from rest_framework import serializers

from apps.portfolio.models import Portfolio, Photo, Comments
from apps.user.serializers import UserSerializer
from apps.core.serializers import SanitizeData

class PortfolioSerializer(SanitizeData):
    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class CommentsSerializer(SanitizeData):
    user = UserSerializer(read_only=True)
    photo_id = serializers.PrimaryKeyRelatedField(source='photo', queryset=Photo.objects.all(), write_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'photo', 'photo_id', 'user', 'text']
        read_only_fields = ['id', 'photo']


class PhotoSerializer(SanitizeData):
    portfolio = serializers.CharField(source='portfolio.name', read_only=True)
    portfolio_id = serializers.PrimaryKeyRelatedField(source='portfolio', queryset=Portfolio.objects.all(),
                                                      write_only=True)
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Photo
        fields = ['id', 'portfolio', 'portfolio_id', 'name', 'description', 'image', 'comments']
        read_only_fields = ['id', 'portfolio', 'comments']

    def validate_portfolio_id(self, value):
        if value.user != self.context['request'].user:
            raise serializers.ValidationError('This is not yours portfolio.')
        return value
