from django.db import models



 
class Lessons(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    tutorial = models.FileField(upload_to='videos/', null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    

class Question(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Question: {self.text} (Lesson: {self.lesson.title})"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Choice: {self.text} ({'Correct' if self.is_correct else 'Wrong'})"



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    