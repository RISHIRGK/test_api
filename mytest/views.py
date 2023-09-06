from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# from rest_framework import serializers
from rest_framework.response import Response
from . import models,serializers
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, serializers


def booklist(request):
    books = models.book.objects.all()
    serializer = serializers.bookserializer(books, many=True)
    return JsonResponse ({"books": serializer.data})
