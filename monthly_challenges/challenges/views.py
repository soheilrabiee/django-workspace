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


def monthly_challenge_by_number(request, month):
    """Takes a number [1,12] and redirects the user to the correct month"""
    months = list(monthly_challenges_text.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    # Using args to add '/month' path to the '/challenges' url
    redirect_path = reverse(viewname="month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    """Checks the dict and returns the value based of month"""
    try:
        output = monthly_challenges_text[month]
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>Invalid month!</h1>")


def index(request):
    """Makes a list of links to the challenges of each month"""
    list_items = ""
    for month in monthly_challenges_text.keys():
        item_path = reverse(viewname="month-challenge", args=[month])
        list_items += f'<li><a href="{item_path}">{month.capitalize()}</a></li>'

    return HttpResponse(f"<ul>{list_items}</ul>")
