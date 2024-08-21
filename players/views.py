from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests
from pathlib import Path
import json
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).parents[1]

@method_decorator(csrf_exempt, name='dispatch')
class AgentInteraction(View):
    def post(self, request):    
          
        load_dotenv(os.path.join(BASE_DIR, '.env'))    
        agent_url = os.getenv('AGENTS_ENDPOINT')
        # agent_url= "http://localhost:8080/predictions/random_agent"
        json_data = json.loads(request.body)
        response = requests.post(agent_url, json=json_data)
        return JsonResponse(response.json())

