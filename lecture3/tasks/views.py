from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    # looking inside the session to see is there already a list of tasks in that session. if there isn't already a list of tasks in the session, then create it. Then set request.session square bracket tasks equal to the empty list. If the user doesn't already have a list of tasks, go ahead and give them an empty list of tasks.
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
    
def add(request):
    # checking request method is POST, meaning if the user submitted some form data. 
    if request.method == "POST":
        # we figure out all the data they submitted and save it inside this form variable. request.POST contains all of the data that the user submitted.
        form = NewTaskForm(request.POST) 
        # We check to see if the form is valid. Did they actually provide a task? Are they providing all the necessary data in the right format?
        if form.is_valid():
            # If so, then we get the task and add it to the list of tasks.
            task = form.cleaned_data["task"]
            # append value of task to request.session["tasks"]
            request.session["tasks"] += [task]
            # redirect to URL in my app
            return HttpResponseRedirect(reverse("tasks:index"))            
        else:
            # if the form is not valid, then we go ahead and render that same add.html file back to them, but we pass in the form that they submitted so that they can see all of the errors they made.
            # this will be returned when server validation doesn't match with user validation
            return render(request, "tasks/add.html", {
                "form": form
            })
    # if the user just tried to get the page rather than submit data to it, then we're just going to render to them an empty form.
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })