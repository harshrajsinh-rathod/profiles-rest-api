from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from  rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        

        an_apiview = [
            "User HTTP methods as functions",
            "Used in django rest-api framework available",
            "Gives better control hopefully",
            "Maps to URLs"
        ]

        return Response({"message": "Hello!","an_apiview": an_apiview}) 

    
    def post(self, request):
        "Creates hello message with input name "
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}.'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request,pk=None):
        return Response({"method":"PUT"})
    
    def patch(self, request,pk=None):
        return Response({"method":"PATCH"})
    
    def delete(self, request,pk=None):
        return Response({"method":"DELETE"})


class HelloViewSets(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            " list, create, update, patch update ", 
            "url mappings",
            "less code"
        ]
        return Response({"message":"Hello!", "a_viewset":a_viewset})

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}.'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        return Response({"http_method":"GET"})

    def update(self, request, pk=None ):
        return Response({"http_method":"PUT"})

    def partial_update(self, request, pk=None):
        return Response({"http_method":"PATCH"})

    def destroy(self, request, pk=None):
        return Response({"http_method":"DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email",)

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):

    authentication_classes= (TokenAuthentication,)
    queryset= models.ProfileFeedItem.objects.all()
    serializer_class = serializers.ProfileFeedItemSerializer
    permissions_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
        )

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)


