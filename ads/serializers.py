from rest_framework import serializers

from .models import Ad


class AdSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source='publisher.username')

    class Meta:
        model = Ad
        fields = '__all__'
        read_only_fields = ('date_added', 'is_published')
        extra_kwargs = {
            'image': {'required': False}
        }


class SearchSerializer(serializers.Serializer):
    search = serializers.CharField()
