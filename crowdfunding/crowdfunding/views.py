from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    def get(self, request):
        return Response(
        {
            "users/": ["GET","POST","DELETE","UPDATE"], 
            "project/": ["GET","POST","DELETE","UPDATE"],
            "pledges/": ["GET","POST","DELETE","UPDATE"],
        }
        )