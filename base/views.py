from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task

# Create your views here.

# def taskList(request):
#     return HttpResponse("Testing the url connection and view function")

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'    # Instead of the default 'object_list'
