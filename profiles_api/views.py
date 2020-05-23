from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions



class HelloApiView(APIView):
    """Hello Api view"""
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        """Returns a list of APIview features"""
        an_apiview=[
            'Uses HTTP methods as function (get,post,patch,dfelete)',
            'is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
    def post(self,request):
        """Create a hello mesage with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a particular update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete n object"""
        return Response({'method':'DELETE'})
class Helloviewset(viewsets.ViewSet):
    """TEst api viewset"""
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        """REturn hello meaasge"""
        a_viewset=[
            'uses action( list,create,retrivre,update,delete)',
            'Automatically maps to URLs using routers',
            'Provide more functionality with less code'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})
    def creaye(self,request):
        """create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid:
            name=serializer.validated_data.get('name')
            message=f'Hello{name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self,request,pk=None):
        """Handle getting an object its ID"""
        return Response({'http_method':'GET'})
    def update(self,request,pk=None):
        """Handle a  an object"""
        return Response({'http_method':'PUT'})
    def partial_update(self,request,pk=None):
        """Handle a part of an object"""
        return Response({'http_method':'PATCH'})
    def destroy(self,request,pk=None):
        """Handkle removing an object"""
        return Response({'http_method':'DELETE'})
class UserProfileViewSet(viewsets.ModelViewSet):
        """Handle creating and updating profiles"""
        serializer_class=serializers.UserProfileSerializer
        queryset=models.UserProfile.objects.all()
        authentication_classes=(TokenAuthentication,)
        permission_classes=(permissions.UpdateOwnProfile,)
