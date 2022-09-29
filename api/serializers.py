from rest_framework import serializers
from myapp.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = "__all__"
		

class CustomVoteField(serializers.Field):
	def to_representation(self, value):
		return value
		
		
class ChoiceSerializer(serializers.ModelSerializer):
	question = serializers.SlugRelatedField(many=False, read_only=False, slug_field="question", queryset= Question.objects.all())	
	votes = CustomVoteField(read_only= True)
	
	class Meta:
		model = Choice
		fields = ["question", "choice", "votes"]
		
		