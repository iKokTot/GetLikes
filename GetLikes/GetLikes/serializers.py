from rest_framework import serializers

class VKExchangeTokenSerializer(serializers.Serializer):
    silent_token = serializers.CharField()
    uuid = serializers.CharField()

class GetUserAlbumSerializer(serializers.Serializer):
    owner_id = serializers.CharField()


class GetUserPhotosSerializer(serializers.Serializer):
    owner_id = serializers.CharField()
    album_id = serializers.CharField()