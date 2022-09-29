from django.shortcuts import render
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import generics
from myapp.models import Question, Choice


class QuestionCreateListView(generics.ListCreateAPIView):
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()
	
	
class QuestionCrudView(
	generics.RetrieveUpdateDestroyAPIView
):
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()
	lookup_field = "id"
	
	
class ChoiceListView(generics.ListCreateAPIView):
	serializer_class = ChoiceSerializer
	queryset = Choice.objects.all()
	
	def perform_create(self, serializer):
		serialized_question = serializer.validated_data.get("question")
		serialized_choice = serializer.validated_data.get("choice")
		
		question = Question.objects.get(question= serialized_question)
		choice, created = question.choice_set.get_or_create(choice= serialized_choice)
		
		if choice:
			choice.votes += 1
			choice.save()
			return
		else:
			serializer.save()
			new_choice = Choice.objects.get(choice= serialized_choice)
			new_choice.votes += 1
			new_choice.save()
			
			
class ChoiceRetrieveView(generics.RetrieveAPIView):
	serializer_class = ChoiceSerializer
	queryset = Choice.objects.all()
	lookup_field = "id"
	
	
class ChoiceUpdateView(generics.UpdateAPIView):
	serializer_class = ChoiceSerializer
	queryset = Choice.objects.all()
	lookup_field = "id"
	
	
class ChoiceDestroyView(generics.DestroyAPIView):
	serializer_class = ChoiceSerializer
	queryset = Choice.objects.all()
	lookup_field = "id"
	
	