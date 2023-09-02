from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from django.db.models import Q
from .models import Ad
from .serializers import AdSerializer, SearchSerializer
from .paginations import StandardSetPagination
from .permissions import IsPublisherOrReadOnly


# Create your views here.
class AdApiView(APIView, StandardSetPagination):
    serializer_class = AdSerializer

    def get(self, request):
        ads = Ad.objects.filter(is_published=True)
        result = self.paginate_queryset(ads, request)
        serializer = AdSerializer(instance=result, many=True)
        return self.get_paginated_response(serializer.data)

        # return Response(serializer.data, status=status.HTTP_200_OK)


class AdCreateApiView(APIView):
    serializer_class = AdSerializer
    parser_classes = MultiPartParser,  
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['publisher'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class AdDetailApiView(APIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsPublisherOrReadOnly]
    parser_classes = (MultiPartParser,)

    def get_obj(self):
        obj = get_object_or_404(Ad.objects.filter(is_published=True), id=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk):
        obj = self.get_obj()
        serializer = AdSerializer(instance=obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_obj()

        serializer = AdSerializer(instance=obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, request, pk):
        obj = self.get_obj()

        obj.delete()
        return Response({"message": "Deleted"})


class AdSearchApiView(APIView):
    @extend_schema(
        parameters=[ 
            SearchSerializer,  
            # OpenApiParameter('q', OpenApiTypes.STR, OpenApiParameter.QUERY)      
            # OpenApiParameter(name='q', location=OpenApiParameter.QUERY, required=False, type=str)
        ]
    )
    def get(self, request):
        q = request.query_params.get('search')  
        # q = request.GET.get('search')

        query_set = Ad.objects.filter(Q(title__icontains=q) | Q(caption__icontains=q))
        serializer = AdSerializer(instance=query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
