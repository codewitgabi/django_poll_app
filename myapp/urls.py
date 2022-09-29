from django.urls import path
from . import views


urlpatterns = [
	path("", views.question, name= "questions"),
	path("vote/<int:question_id>", views.vote, name= "vote"),
]