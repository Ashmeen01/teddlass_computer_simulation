from django.urls import path

from . import views


app_name = 'core'

urlpatterns = [
    # index page url
    path('', views.index, name="index"),
    # admin-dashboard. url
    path('dashboard/', views.dashboard, name="dashboard"),
    # lesson table-list url
    path('lessons/', views.lessons_list, name='lessons'),
    # create-lesson url
    path('lessons/create/', views.create_lesson, name='create-lesson'),
    # update lesson url
    path('lessons/update/<int:pk>/', views.update_lesson, name='update-lesson'),
    # lesson details url
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson-detail'),
    # from mail url
    path('contact/', views.contact_view, name='contact'),
    # lessons list url
    path('lessons-list/', views.lessons, name='lessons-list'),
    # test lesson url
    path('lesson/<int:lesson_id>/test/', views.lesson_test, name='lesson-test'),
    # submit test url
    path('lesson/<int:lesson_id>/test/submit/', views.submit_test, name='submit-test'),
]
