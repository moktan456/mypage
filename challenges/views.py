from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.


# def jan(request):
#     return HttpResponse("Stop fucking around!")


# def feb(request):
#     return HttpResponse("Walk for at least 20 minutes every day")


# def march(request):
#     return HttpResponse("Learn Python")

# Dynamic values for each month
monthly_challenges = {
    "january": "Productivity Powerhouse",
    "february": "Content Creator",
    "march": "Mind & Body Detox",
    "april": "Financial Fitness",
    "may": "Reading Renaissance",
    "june": "Early Bird Challenge",
    "july": "Embrace the Chill",
    "august": "Mindful Moderation",
    "september": "Learning Quest",
    "october": "Gratitude Glow-Up",
    "november": "Digital Detox",
    "december": "Spreading Holiday Cheer"
}


def montly_challenge_by_month(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponse("Invalid month choice")
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/"+redirect_month)


# def monthly_challenge(request, month):
#     challenge_txt = None
#     if month == "january":
#         challenge_txt = "Stop fucking around"
#     elif month == "february":
#         challenge_txt = "Walk for at least 20 minutes every day"
#     elif month == "march":
#         challenge_txt = "Learn Python"
#     else:
#         return HttpResponseNotFound("This month is not support")
#     return HttpResponse(challenge_txt)
def monthly_challenge(request, month):
    try:
        challenge_txt = monthly_challenges[month]
        return HttpResponse(challenge_txt)
    except:
        return HttpResponse("This month is not supported")
