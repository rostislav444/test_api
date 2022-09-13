from rest_framework import serializers

from apps.portfolio.models import Portfolio, Photos, Comments
from apps.user.serializers import UserSerializer


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']


class CommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    photo_id = serializers.PrimaryKeyRelatedField(source='photo', queryset=Photos.objects.all(), write_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'photo', 'photo_id', 'user', 'text']
        read_only_fields = ['id', 'photo']


class PhotosSerializer(serializers.ModelSerializer):
    portfolio = PortfolioSerializer(read_only=True)
    portfolio_id = serializers.PrimaryKeyRelatedField(source='portfolio', queryset=Portfolio.objects.all(),
                                                      write_only=True)
    comments = CommentsSerializer(many=True)

    class Meta:
        model = Photos
        fields = ['id', 'portfolio', 'portfolio_id', 'name', 'description', 'image', 'comments']
        read_only_fields = ['id', 'portfolio', 'comments']

    def validate_portfolio_id(self, value):
        if value.user != self.context['request'].user:
            raise serializers.ValidationError('This is not yours portfolio.')
        return value
