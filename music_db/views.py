from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response

from music_db.models import Music
from music_db.serializers import MusicSerializer


# @api_view(['GET'])
# def get_music(request):
#     """Get all music"""
#     musics = Music.objects.all()
#     serializer = MusicSerializer(musics, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def music_detail(request):
#     try:
#         music = Music.object.get(id=id)
#         serializer = MusicSerializer(music, many=False)
#         return Response(serializer.data)
#     except Music.DoesNotExist:
#         raise Http404
#
#
# @api_view(['POST'])
# def music_create(request):
#     serializer = MusicSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MusicListView(ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


# class CreateAPIViwe:



class MusicCreateView(CreateAPIView):
    serializer_class = MusicSerializer


class MusicUpdateView(UpdateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicDetailView(RetrieveAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


class MusicDeleteView(DestroyAPIView):
    lookup_field = 'id'
    queryset = Music.objects.all()
    serializer_class = MusicSerializer








