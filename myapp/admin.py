from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
	model = Choice
	
	
class QuestionAdmin(admin.ModelAdmin):
	list_display = ["question"]
	list_filter = ["question"]
	search_fields = ["question"]
	inlines = [ChoiceInline]
	
	
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)