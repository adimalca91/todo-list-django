from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy                # Redirects the user to a certain part of our application 

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
    
'''
By default the CreateView already gives us a ModelForm to work with. So, it will take our Task Model
and it will create all the fields by default for us, therefore we need to specify what fields we want in our Form.
Also when we create an item / a task I want you to be redirected to a different url - use "succecc_url" attribute.
Note - we either need the 'field' attribute or we can create our own ModelForm and just set the 'form_class' 
attribute to the ModelForm we created. Here we use the 'fields' attribute instead.
'''
class TaskCreate(CreateView):
    # Default template is task_form.html
    model = Task
    fields = '__all__'  # We want to list out all the items from the Task Model in the Form
    success_url = reverse_lazy('tasks') # This parameter is the url name attribute from utls.py
    
'''
This view is supposed to take in an item / a task, it suppose to pre-fill a form, and then once we
submit it, just like the CreateView creates an item then the UpdateView will modify the data.

'''
class TaskUpdate(UpdateView):
    # Default template is also task_form.html
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')