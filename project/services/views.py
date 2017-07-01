from rest_framework_mongoengine import generics

from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer


class ListCreateProvidersView(generics.ListCreateAPIView):
    serializer_class = ProviderSerializer

    def get_queryset(self):
        queryset = Provider.objects
        # concatenated_point = self.request.query_params.get('service_at', None)
        # if concatenated_point is not None:
        #     point = concatenated_point.split(',')
        #     if len(point) == 2:
        #         loc = list(map(float, point))
        #         print(loc)
        #         queryset = queryset.filter(service_area__geo_intersects=loc)
        return queryset


class RetrieveUpdateDeleteProviderView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProviderSerializer

    def get_object(self):
        primary_key = self.kwargs.get('pk')
        return Provider.objects(id=primary_key).first()


class ListCreateServiceArea(generics.ListCreateAPIView):
    serializer_class = ServiceAreaSerializer
    # queryset = ServiceArea.objects

    def get_queryset(self):
        queryset = ServiceArea.objects
        concatenated_point = self.request.query_params.get('service_at', None)
        if concatenated_point is not None:
            point = concatenated_point.split(',')
            if len(point) == 2:
                loc = list(map(float, point))
                print(loc)
                queryset = queryset.filter(area__geo_intersects=loc)
        return queryset


class RetrieveUpdateDeleteServiceAreaView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceAreaSerializer

    def get_object(self):
        primary_key = self.kwargs.get('pk')
        return ServiceArea.objects(id=primary_key).first()
