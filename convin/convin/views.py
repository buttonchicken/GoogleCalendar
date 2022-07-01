from django.views.generic.base import TemplateView
import json
import os
from .utils import *
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND)
from datetime import date,timedelta
 
class Home(TemplateView):
    template_name = 'home.html'

class GetEvents(APIView):
    def get(self,request):
        l = get_events()
        events = json.dumps(l)
        os.remove("token.json")
        return Response({'Payload':events},status=HTTP_200_OK)