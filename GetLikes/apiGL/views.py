from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from GetLikes.serializers import VKExchangeTokenSerializer, GetUserAlbumSerializer,GetUserPhotosSerializer
import requests
from rest_framework import status
from apiGL.models import UserProfile

SOCIAL_AUTH_VK_OAUTH2_KEY = '51822829'
SOCIAL_AUTH_VK_OAUTH2_SECRET = '1BfQugR1o4b3sS3xg8Gc'
access_token_app = '66142d1666142d1666142d16256502edfb6661466142d160398892c2135f5028b2c57b3'

# Create your views here.
def index(request):
    return HttpResponse(
        '<!DOCTYPE html > <head> <metacharset = "UTF-8"> <title> Главная страница </title> </head> <body> <h1> Главная страница </h1> <br> <p><a href = "https://oauth.vk.com/authorize?client_id=51822829&redirect_uri=https://localhost&scope=12&display=popup"> Ссылка </p> </body> </html>'
    )

class VKExchangeTokenView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VKExchangeTokenSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        vk_version = '5.131'
        silent_token = serializer.validated_data['silent_token']
        service_token = SOCIAL_AUTH_VK_OAUTH2_KEY
        uuid = serializer.validated_data['uuid']

        url = "https://api.vk.com/method/auth.exchangeSilentAuthToken"
        params = {
            "v": vk_version,
            "token": silent_token,
            "access_token": service_token,
            "uuid": uuid
        }

        response = requests.post(url, data=params)
        response_data = response.json()
        print(response_data)

        # Проверка наличия пользователя в базе данных
        vk_user_id = response_data.get('user_id')
        user_profile, created = UserProfile.objects.get_or_create(vk_user_id=vk_user_id)

        # Обновление данных пользователя
        user_profile.access_token = response_data.get('access_token')
        user_profile.email = response_data.get('email')  # Замените на актуальное поле

        user_profile.save()

        return Response(response_data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

class GetUserAlbum(APIView):
    def get(self, request, *args, **kwargs):
        serializer = GetUserAlbumSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        owner_id = serializer.validated_data['owner_id']

        url = "https://api.vk.com/method/photos.getAlbums"

        params = {
            "access_token": access_token_app,
            'owner_id': owner_id,
            'need_system': 1,
            'need_covers': 1,
            'v': 5.199,
        }

        response = requests.post(url, data=params)
        response_data = response.json()
        return Response(response_data)

class GetUserPhotos(APIView):

    def get(self, request, *args, **kwargs):
        serializer = GetUserPhotosSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        owner_id = serializer.validated_data['owner_id']
        album_id = serializer.validated_data['album_id']

        url = "https://api.vk.com/method/photos.get"

        params = {
            "access_token": access_token_app,
            'owner_id': owner_id,
            'album_id': album_id,
            'need_system': 1,
            'need_covers': 1,
            'v': 5.199,
        }

        response = requests.post(url, data=params)
        response_data = response.json()
        return Response(response_data)