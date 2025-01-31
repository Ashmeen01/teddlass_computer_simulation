from django.shortcuts import render, redirect
from authentication . models import User
from django.contrib import messages
from .models import Lessons, Contact, Choice, Question
from .forms import LessonsForm
import sweetify
from .forms import ContactForm
from django.urls import reverse
import logging

# Create your views here.

def index(request):

    return render(request, 'contents/index.html')


def dashboard(request):
    users = User.objects.all()
    return render(request, 'contents/admin/dashboard.html', {'users': users})



# View for listing all lessons
def lessons_list(request):
    lessons = Lessons.objects.all()
    return render(request, 'contents/admin/lessons.html', {'lessons': lessons})

# View for creating a new lesson
def create_lesson(request):
    if request.method == 'POST':
        form = LessonsForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Lesson created successfully!')
            return redirect('core:lessons')
    else:
        form = LessonsForm()

    return render(request, 'contents/admin/create-lesson.html', {'form': form})

# View for editing an existing lesson
def update_lesson(request, pk):
    lesson = Lessons.objects.get(id=pk)
    if request.method == 'POST':
        form = LessonsForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            sweetify.success(request, 'Lesson updated successfully!')
            return redirect('core:lessons')
    else:
        form = LessonsForm(instance=lesson)
        return render(request, 'contents/admin/update-lesson.html', {'form': form, 'lesson': lesson})


def lesson_detail(request, pk):
    lesson = Lessons.objects.get(id=pk)
    return render(request, 'contents/admin/lessons-details.html', {'lesson': lesson})



# Lesson test view
def lesson_test(request, lesson_id):
    try:
        lesson = Lessons.objects.get(id=lesson_id)
    except Lessons.DoesNotExist:
        return render(request, 'contents/admin/test-result.html', {'error': 'Lesson not found.'})

    questions = lesson.questions.prefetch_related('choices')

    if not questions.exists():
        return render(request, 'contents/admin/lesson-test.html', {'lesson': lesson, 'error': 'No questions available for this lesson.'})

    return render(request, 'contents/admin/lesson-test.html', {
        'lesson': lesson,
        'questions': questions,
        'submit_url': reverse('core:submit-test', args=[lesson_id])  # Pass the submit URL
    })




# Submit test view
logger = logging.getLogger(__name__)
def submit_test(request, lesson_id):
    if request.method == 'POST':
        try:
            lesson = Lessons.objects.get(id=lesson_id)
            questions = lesson.questions.prefetch_related('choices')
        except Lessons.DoesNotExist:
            return redirect('lesson-test', lesson_id=lesson_id)

        score = 0
        total_questions = questions.count()

        logger.info(f"Processing test for lesson: {lesson.title}")

        for question in questions:
            selected_option = request.POST.get(f'question-{question.id}')
            logger.info(f"Selected option for Question {question.id}: {selected_option}")

            if selected_option:
                try:
                    choice = Choice.objects.get(id=int(selected_option))
                    logger.info(f"Choice Text: {choice.text}, Is Correct: {choice.is_correct}")

                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    logger.warning(f"Choice with ID {selected_option} does not exist.")
                    continue  # Ignore invalid choice IDs

        percentage = (score / total_questions) * 100 if total_questions > 0 else 0

        logger.info(f"Test completed: Score={score}, Total Questions={total_questions}, Percentage={percentage}")

        return render(request, 'contents/admin/test-result.html', {
            'lesson': lesson,
            'score': score,
            'total_questions': total_questions,
            'percentage': round(percentage, 2)
        })

    return redirect('core:lesson-test', lesson_id=lesson_id)




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            messages.success(request, "Your message has been saved. Thank you!")
        else:
            messages.error(request, "There was an error with your submission. Please try again.")
    else:
        form = ContactForm()

    return render(request, 'contents/index.html', {'form': form})


def lessons(request):
    lessons = Lessons.objects.all()
    return render(request, 'contents/admin/lessons-list.html', {'lessons': lessons})


