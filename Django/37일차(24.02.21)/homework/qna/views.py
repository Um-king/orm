from django.shortcuts import render
from django.http import HttpResponse


def qna(request):
    return HttpResponse("qna Page")


def qnadetails(request, pk):
    return HttpResponse(f"qna Details Page: {pk}")