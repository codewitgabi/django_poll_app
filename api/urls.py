from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	path("questions_list/", views.QuestionCreateListView.as_view(), name= "questions_list"),
	path("question_detail_view/<int:id>/", views.QuestionCrudView.as_view(), name= "question_detail_view"),
	path("choice_list/", views.ChoiceListView.as_view(), name= "choice_list"),
	path("get_choice/<int:id>/", views.ChoiceRetrieveView.as_view(), name= "get_choice"),
	path("update_choice/<int:id>/", views.ChoiceUpdateView.as_view(), name= "update_choice"),
	path("delete_choice/<int:id>/", views.ChoiceDestroyView.as_view(), name= "delete_choice"),
	
]

urlpatterns = format_suffix_patterns(urlpatterns)