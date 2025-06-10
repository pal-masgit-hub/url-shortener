from django.urls import path, include
from .views import *

urlpatterns = [
    path("", make_url_short, name="make_url_short"),
    path("redirect_url/<url>", view_url, name="view_url"),
    path("red/<url>/", redirect_url, name="redirect_url"),
    path("random/", random_url, name="random"),

]
