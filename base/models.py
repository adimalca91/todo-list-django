from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# One user can have many tasks - one to many relationship.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    # Set default ordering
    # Order the model by the complete status - so any complete tasks should be sent to the bottom of the list b/c
    # they are done and we don't need to focus on them anymore
    '''
    This is how we can order a queryset - whenever we are returning multiple items order it by this
    value here
    '''
    class Meta:
        ordering = ['complete']
        