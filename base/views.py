from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

# Create your views here.

# def taskList(request):
#     return HttpResponse("Testing the url connection and view function")

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'   # Instead of the default 'object_list' - this is the queryset of the tasks (python representation of the model)


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'   # Instead of the default 'object'
    # template_name = 'base/task.html' # This allows us to change the default naming of the html template
    