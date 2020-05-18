from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Hello Api view"""
    def get(self,request,format=None):
        """Returns a list of APIview features"""
        an_apiview=[
            'Uses HTTP methods as function (get,post,patch,dfelete)',
            'is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
