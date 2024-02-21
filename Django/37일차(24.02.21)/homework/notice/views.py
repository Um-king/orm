from django.shortcuts import render
from django.http import HttpResponse


# def free(request):
#     return HttpResponse("free Page")


# def freedetails(request, pk):
#     return HttpResponse(f"free Details Page: {pk}")


# def onenone(request):
#     return HttpResponse("onenone Page")


# def onenonedetails(request, pk):
#     return HttpResponse(f"onenone Details Page: {pk}")

def details(request, word, pk):
    return HttpResponse(f"{word} Details Page: {pk}")
