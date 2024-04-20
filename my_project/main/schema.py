import graphene
from graphene_django.types import DjangoObjectType
from .models import Artist, Album, Song

class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist

class AlbumType(DjangoObjectType):
    class Meta:
        model = Album

class SongType(DjangoObjectType):
    class Meta:
        model = Song

class Query(graphene.ObjectType):
    all_artists = graphene.List(ArtistType)
    all_albums = graphene.List(AlbumType)
    all_songs = graphene.List(SongType)

    def resolve_all_artists(self, info, **kwargs):
        return Artist.objects.all()

    def resolve_all_albums(self, info, **kwargs):
        return Album.objects.all()

    def resolve_all_songs(self, info, **kwargs):
        return Song.objects.all()

schema = graphene.Schema(query=Query)
