from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("story/<int:story_id>/", views.story, name="story"),
    path("check/",views.check_vocabulary, name="check_vocabulary"),
    path("save/", views.save_vocabulary, name="save_vocabulary"),
    path("vocabulary/", views.vocabulary, name="vocabulary"),
    path("stories/", views.stories, name="stories")
]