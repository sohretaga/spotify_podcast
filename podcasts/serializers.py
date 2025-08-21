from rest_framework import serializers


class ShowSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    publisher = serializers.CharField()
    description = serializers.CharField()
    languages = serializers.ListField()
    media_type = serializers.CharField()
    total_episodes = serializers.IntegerField()
    images = serializers.ListField()
    external_urls = serializers.DictField()
    available_markets = serializers.ListField()


class EpisodeSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    release_date = serializers.CharField()
    duration_ms = serializers.IntegerField()
    explicit = serializers.BooleanField()
    audio_preview_url = serializers.CharField(allow_null=True)
    images = serializers.ListField()
    external_urls = serializers.DictField()
    languages = serializers.ListField()
