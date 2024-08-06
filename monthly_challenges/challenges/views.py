from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.urls import reverse

monthly_challenges_text = {
    "january": "Here is the challenge for january!",
    "february": "Here is the challenge for february!",
    "march": "Here is the challenge for march!",
    "april": "Here is the challenge for april!",
    "may": "Here is the challenge for may!",
    "june": "Here is the challenge for june!",
    "july": "Here is the challenge for july!",
    "august": "Here is the challenge for august!",
    "september": "Here is the challenge for september!",
    "october": "Here is the challenge for october!",
    "november": "Here is the challenge for november!",
    "december": "Here is the challenge for december!",
}
# Create your views here.


def monthly_challenge(request, month):
    if month in monthly_challenges_text:
        return HttpResponse(f"{monthly_challenges_text[month]}")
    return HttpResponseNotFound("Incorrect month!")
