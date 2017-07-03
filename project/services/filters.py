'''Filter for geo location'''
from django_filters.rest_framework import DjangoFilterBackend


class LocationFilter(DjangoFilterBackend):
    '''
    Returns only those areas that contain given location
    '''
    def filter_queryset(self, request, queryset, view):
        concatenated_point = request.query_params.get('service_at', None)
        if concatenated_point is not None:
            point = concatenated_point.split(',')
            if len(point) == 2:
                loc = list(map(float, point))
                print(loc)
                queryset = queryset.filter(area__geo_intersects=loc)
        return queryset
