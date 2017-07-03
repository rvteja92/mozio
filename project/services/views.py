from rest_framework_mongoengine import generics

from .filters import LocationFilter
from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer


class ListCreateProvidersView(generics.ListCreateAPIView):
    '''
    get:
    Return the list of all the service providers with details

    post:
    Create a service provider
    '''
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
    '''
    get:
    Return a `service provider` with full details

    patch:
    Update the provided fields of the `service provider`

    put:
    Update the `service provider` (all fields required)

    delete:
    Delete the `service provider` with specified id
    '''
    serializer_class = ProviderSerializer

    def get_object(self):
        primary_key = self.kwargs.get('pk')
        return Provider.objects(id=primary_key).first()


class ListCreateServiceArea(generics.ListCreateAPIView):
    '''
    get:
    Return the list of all the service areas and their details.
    Areas are filtered with parameter `service_at` with value
    `<latitude>,<longitude>`

    post:
    Create a service area
    '''
    serializer_class = ServiceAreaSerializer
    filter_backends = (LocationFilter,)
    # queryset = ServiceArea.objects

    def get_queryset(self):
        queryset = ServiceArea.objects
        return queryset


class RetrieveUpdateDeleteServiceAreaView(generics.RetrieveUpdateDestroyAPIView):
    '''
    get:
    Return a service area with full details

    patch:
    Update the provided fields of the service area

    put:
    Update the service area (all fields required)

    delete:
    Delete the service area with specified id
    '''
    serializer_class = ServiceAreaSerializer

    def get_object(self):
        primary_key = self.kwargs.get('pk')
        return ServiceArea.objects(id=primary_key).first()
