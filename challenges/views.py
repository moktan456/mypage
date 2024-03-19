from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
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
    "december": None
}


def index(request):
   # list_items = ""
    months = list(monthly_challenges.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        "months": months
    })


def montly_challenge_by_month(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponse("Invalid month choice")
    redirect_month = months[month-1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


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
        return render(request, "challenges/challenge.html", {
            "month": month,
            "challenge": challenge_txt
        })
       # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponse("<h1>This month is not supported</h1>")
