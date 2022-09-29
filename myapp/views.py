from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice
from django.http import JsonResponse


def question(request):
	questions = Question.objects.all()
	context = {
		"questions": questions
	}
	return render(request, "question.html", context)
	
	
def vote(request, question_id):
	question = get_object_or_404(Question, id= question_id)
	if request.method == "POST":
		choice = request.POST.get("answer")
		if choice:
			obj = Choice.objects.get(question_id= question_id, choice= choice)
			obj.votes += 1
			obj.save()
		else:
			pass
		
		return JsonResponse({"choice": choice})
		return redirect("questions")
	context = {"question": question}
	return render(request, "vote.html", context)