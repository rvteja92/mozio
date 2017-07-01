'''Serializer definitions'''

from rest_framework_mongoengine import serializers

from .models import Provider, ServiceArea


class ProviderSerializer(serializers.DocumentSerializer):
    '''Serializer for Provider model'''

    class Meta:
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(serializers.DocumentSerializer):
    '''Serializer for ServiceArea model'''
    provider = ProviderSerializer(read_only=True, source='Provider')

    class Meta:
        model = ServiceArea
        fields = '__all__'
