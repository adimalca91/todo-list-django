from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy  # Redirects the user to a certain part of our application

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# Create your views here.
'''
Bu default this LoginView already provides us with a form
'''
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    

''' These are going to be the CRUD operations '''

# def taskList(request):
#     return HttpResponse("Testing the url connection and view function")

'''
To restrict our Task List view we use the MIXIN.
So, if out user is NOT logged in it redirects us utomatically, so we need to add something in settings.py - 
LOGIN_URL and then we enter the address to redirect the user if they are NOT logged in / authenticated.
'''
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'   # Instead of the default 'object_list' - this is the queryset of the tasks (python representation of the model)
    
    '''
    Also - we need to make sure that each user sees his own tasks and that one user can't log-in on his
    username and password, but see other user's tasks.
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

    
'''       
To restrict the user from getting the Task Detail view we use the MIXIN.
MUST be added before the View.
'''
class TaskDetail(LoginRequiredMixin, DetailView):
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
class TaskCreate(LoginRequiredMixin, CreateView):
    # Default template is task_form.html
    model = Task
    fields = '__all__'  # We want to list out all the items from the Task Model in the Form
    success_url = reverse_lazy('tasks') # This parameter is the url name attribute from utls.py
    
'''
This view is supposed to take in an item / a task, it suppose to pre-fill a form, and then once we
submit it, just like the CreateView creates an item then the UpdateView will modify the data.

'''
class TaskUpdate(LoginRequiredMixin, UpdateView):
    # Default template is also task_form.html
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    

'''
Renders a confirmation page to ensure you want to delete the task and then when we send a POST
request it will delete that item.
'''
class TaskDelete(LoginRequiredMixin, DeleteView):
    # Default template is also task_confirm_delete.html
    model = Task
    context_object_name = 'task' # The default is 'object2'
    success_url = reverse_lazy('tasks')
