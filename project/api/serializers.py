from rest_framework.serializers import ModelSerializer

from api.models import Advert


class AdvertSerializer(ModelSerializer):
    class Meta:
        model = Advert
        fields = ('id', 'title', 'description', 'owner',
                  'owner_email', 'created_at',)
        read_only_fields = ('id', 'created_at',)
