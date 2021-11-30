from rest_framework import serializers
from friend import models as friend
from utitilities import utils


class FriendshipSerializer(serializers.ModelSerializer):
    """
    Serializer for Friendship
    """

    _from = serializers.UUIDField(required=False)

    def to_internal_value(self, validated_data):
        data = super(FriendshipSerializer, self).to_internal_value(validated_data)
        if utils.get_current_user():
            data["_from"] = utils.get_current_user()
        return data

    def to_representation(self, instance):
        data = super(FriendshipSerializer, self).to_representation(instance)
        data["_to"] = {
            "id": instance._to.id,
            "name": instance._to.name,
            "email": instance._to.email,
        }
        data["_from"] = {
            "id": instance._from.id,
            "name": instance._from.name,
            "email": instance._from.email,
        }

    class Meta:
        fields = "__all__"
        model = friend.Friendship
