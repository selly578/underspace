from django.urls import path,include
from .views import *

urlpatterns = [
    path("", index,name="index"),
    path("b/<str:name>/", board,name="board"),
    path("b/<str:name>/<int:id>",post,name="post"),
    path("rule/",rule,name="rule"),
    path("about/",about,name="about"),
]
