from django.shortcuts import render, redirect
from .models import Dojo, Ninja
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "dojos": Dojo.objects.all()
    }
    return render(request, "index.html", context)

def add_dojo(request):
    post = request.POST
    Dojo.objects.create(
        name = post["name"],
        city = post["city"],
        state = post["state"]
    )
    return redirect("/")

def add_ninja(request):
    errors = Ninja.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for error in errors.values():
            print(error)
            messages.error(request, error)
        return redirect("/")

    post = request.POST
    selected_dojo = Dojo.objects.get(id = post["dojo_id"])
    Ninja.objects.create(
        first_name = post["first_name"],
        last_name = post["last_name"],
        dojo = selected_dojo
    )
    return redirect("/")



