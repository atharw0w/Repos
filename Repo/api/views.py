import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from dotenv import load_dotenv

load_dotenv('.env')


@api_view(['GET'])
def getRepos(request, user):
    try:
        get_url = f'{os.environ["REPO_API"]}/{user}/repos'
        response = requests.get(get_url)
        response = response.json()

        if type(response) == dict and response['message'] == 'Not Found':
            return Response({"error": 'invalid username'}, status=status.HTTP_404_NOT_FOUND)

        return Response(response, status=200)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getLanguages(request, user, repo):
    try:
        get_url = f'{os.environ["REPO_API"]}/{user}'
        response = requests.get(get_url)
        response = response.json()

        if response.get('message', '') == 'Not Found':
            return Response({"error": 'invalid username'}, status=status.HTTP_404_NOT_FOUND)

        get_url = f'{os.environ["LANG_API"]}/{user}/{repo}/languages'
        response = requests.get(get_url)
        response = response.json()

        if response.get('message', '') == 'Not Found':
            return Response({"error": 'invalid repository'}, status=status.HTTP_404_NOT_FOUND)

        return Response(response, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": e}, status=status.HTTP_400_BAD_REQUEST)
