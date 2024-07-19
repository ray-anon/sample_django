from django.shortcuts import render 
from django.http import HttpResponse , Http404 , HttpResponseNotFound , HttpResponseRedirect 
from django.urls import reverse

monthly_challenges = {
    "january": "hello january",
    "february": "hello february",
    "march": "hello march",
    "april": "hello april",
    "may": "hello may",
    "june": "hello june",
    "july": "hello july",
    "august": "hello august",
    "september": "hello september",
    "october": "hello october",
    "november": "hello november",
    "december": "hello december",
}

# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge" , args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request , month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month ")
    forward_month = months[month - 1]
    redirect_path = reverse("month-challenge" , args=[forward_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request , month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported")