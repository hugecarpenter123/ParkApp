from django.shortcuts import render
from rest_framework.response import Response
from .serializers import LocationSerializer, SectionSerializer, SpotSerializer, LocationSearchSerializer, MotionSerializer
from parking.models import Location, Section, Spot, Motion
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

@api_view(["GET", "PUT"])
def parking_space_api(request, pk=None, *args, **kwargs):
    if request.method == "GET":
        if pk:
            object = get_object_or_404(Location, pk=pk)
            serializer = LocationSerializer(instance=object, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":
        if pk:
            object = get_object_or_404(Spot, pk=pk)
            data = {
                'section': object.section.id,
                'row': object.row,
                'column': object.column,
                'status': request.data['status']
            }

            serializer = SpotSerializer(instance=object, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def locations_api(request):
    if request.method == "GET":
        print(request.GET)
        if request.GET.get('search'):
            query = request.GET.get('search')
            objects = Location.objects.filter(name__icontains=query)
            serializer = LocationSearchSerializer(instance=objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            objects = Location.objects.all()
            serializer = LocationSearchSerializer(instance=objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def statistics_api(request, pk=None, *args, **kwargs):
    print("statistics api called()")
    if request.method == "GET":
        print("method: GET")
        if pk:
            print("pk:", pk)
            location = Location.objects.get(pk=pk)
            # print("location:", location)
            objects = location.motion_set.all()
            # print("objects:", objects)
            serializer = MotionSerializer(instance=objects, many=True)
            print('serializer:', serializer)
            print('serializer.data:', serializer.data)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            objects = Motion.objects.all()
            serializer = MotionSerializer(instance=objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
