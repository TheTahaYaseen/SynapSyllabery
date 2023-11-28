from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    
    path('register', views.register_view, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    
    path('learn', views.learn_view, name="learn"),
    path('quizzes', views.quizzes_view, name="quizzes"),
    path('add_word', views.add_word_view, name="add_word"),
    path('my_progress', views.my_progress_view, name="my_progress"),
    path('settings', views.settings_view, name="settings"),
]