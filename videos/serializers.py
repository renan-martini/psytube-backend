from rest_framework import serializers

from users.serializers import UserSerializer
from reviews.serializers import ReviewSerializer
from .models import Video
from django.core.exceptions import ObjectDoesNotExist


class VideoSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        exclude = ["downloads", "link"]

    def create(self, validated_data):

        movie, _ = Video.objects.get_or_create(
            link=validated_data["link"], defaults={**validated_data}
        )

        movie.downloads = movie.downloads + 1
        movie.save()
        return movie


class ListTopVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ["users"]


class ListVideoDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        exclude = ["users"]