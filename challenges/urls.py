from django.urls import path
from . import views

#  path("january", views.jan),
#     path("february", views.feb),
#     path("march", views.march),


urlpatterns = [
    path("<int:month>", views.montly_challenge_by_month),
    path("<str:month>", views.monthly_challenge)
]
