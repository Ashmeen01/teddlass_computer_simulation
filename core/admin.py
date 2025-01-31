from django.contrib import admin
from .models import Lessons, Contact, Choice, Question

class LessonsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    search_fields = ('title',)
    list_filter = ('created_on',)

admin.site.register(Lessons, LessonsAdmin)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('submitted_at',)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'lesson')
    search_fields = ('text',)
    list_filter = ('lesson',)
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question', 'is_correct')
    list_filter = ('is_correct', 'question__lesson')
    search_fields = ('text',)