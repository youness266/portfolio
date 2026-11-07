from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Story, Content
from django.contrib.auth.decorators import login_required
import json

# Create your views here.

def index(request):
    return render(request, "veloria_app/index.html")

def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"veloria_app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "veloria_app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "veloria_app/register.html",{
                "message": "Passwords must match."
            })
        
        try:
            user = User.objects.create_user(username,email,password)
            user.save()
        except IntegrityError:
            return render(request, "veloria_app/register.html", {
                "message": "username already taken."
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "veloria_app/register.html")



# displaying the story

def story(request, story_id):
    if not request.user .is_authenticated:
        return render(request,"veloria_app/login.html")
    
    story_obj = Story.objects.get(id=story_id)
    sentences = Content.objects.filter(story_id=story_id).order_by("id")

    return render(request, "veloria_app/story.html", {
        "story" : story_obj,
        "sentences" : sentences
    })


#Checking the vocabulary
@login_required
def check_vocabulary(request):
    if request.method == "GET":
        sentence_id = request.GET.get("sentence_id")
        status = "ok"
        user = request.user
        vocab_ids = user.vocabulary_ids or []

        if sentence_id in vocab_ids:
            status = "already saved"
        
        return JsonResponse({"status": status})




# Saving vocabulary
@login_required
def save_vocabulary(request):
    if request.method == "POST":
        data = json.loads(request.body)
        sentence_id = data.get("sentence_id")
        status = "already saved"

        user = request.user
        vocab_ids = user.vocabulary_ids or []
        if sentence_id not in vocab_ids:
            vocab_ids.append(sentence_id)
            user.vocabulary_ids = vocab_ids
            user.save()
            status = "ok"
        
        return JsonResponse({"status": status})


@login_required
def vocabulary(request):
    if request.method == "GET":
        user = request.user
        vocab_ids = user.vocabulary_ids or []
        vocab_ids = [int(i) for i in vocab_ids]

        sentences = Content.objects.filter(id__in=vocab_ids)

        return render(request, "veloria_app/vocabulary.html", {
            "sentences": sentences
        })
        

def stories(request):
    if request.method == "GET":

        a1_stories = Story.objects.filter(level="A1")
        a2_stories = Story.objects.filter(level="A2")
        b1_stories = Story.objects.filter(level="B1")
        b2_stories = Story.objects.filter(level="B2")
        c1_stories = Story.objects.filter(level="C1")

        return render(request, "veloria_app/stories.html", {
            "a1_stories": a1_stories,
            "a2_stories": a2_stories,
            "b1_stories": b1_stories,
            "b2_stories": b2_stories,
            "c1_stories": c1_stories
        })

        