from django.urls import path
from . import views


app_name = 'user_auth'

urlpatterns = [
    # sign-up url
    path('create-account/', views.create_account, name="create-account"),
    # sign-in url
    path('sign-in/', views.login_user, name='sign-in'),
    # sign-out url
    path('logout/', views.logout_user, name='logout'), 
]
