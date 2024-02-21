from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('잘 나가는 상품 10개 소개')


def about(request):
    return HttpResponse('회사 소개')


def contact(request):
    return HttpResponse('오시는 길')