from django.shortcuts import render
import requests
from django.http.response import JsonResponse
# Create your views here.
api_key='584f5f7739d24380af0c8ac6ac9f4c8f'
def home(request):
    url=f'https://newsapi.org/v2/top-headlines/sources?category=business&apiKey={api_key}'
    response = requests.get(url)
    response= response.json()
    return JsonResponse({'data':response})
