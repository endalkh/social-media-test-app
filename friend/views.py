from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from rest_framework import generics
from friend import models as friend, serializers
from utitilities import exception_handler, utils, pagination
from django.db import models


class Friend_LA(generics.ListCreateAPIView):
    """
    An API to LIST and ADD Friend(LA~ list add)
    """

    queryset = friend.Friendship.objects.all()
    serializer_class = serializers.FriendshipSerializer
    pagination_class = pagination.MyOffsetPagination
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filterset_fields = [
        "_from__name",
        "_to__name",
        "_from__email",
        "_to__email",
    ]
    search_fields = [
        "_from__name",
        "_to__name",
        "_from__email",
        "_to__email",
    ]

    def get_queryset(self):
        return friend.Transaction.objects.filter(
            models.Q(_from=utils.get_current_user().id)
            | models.Q(_to=utils.utils.get_current_user().id)
        )


class Friend_RUD(generics.RetrieveUpdateDestroyAPIView):
    """
    An API to Retrieve, Update and Delete Friend(RUD~Retrieve, Update, Delete )
    """

    queryset = friend.Friendship.objects.all()
    serializer_class = serializers.FriendshipSerializer
    pagination_class = pagination.MyOffsetPagination
    lookup_field = "id"

    def delete(self, request, id=None, *args, **kwargs):
        result = exception_handler.delete_exception_handler(
            self, request, id=id, *args, **kwargs
        )

        return result
