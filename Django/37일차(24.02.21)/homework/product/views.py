from django.shortcuts import render
from django.http import HttpResponse


def product(request):
    return HttpResponse("product Page")


def productdetails(request, pk):
    return HttpResponse(f"product Details Page: {pk}")