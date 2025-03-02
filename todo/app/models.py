from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=255)
    todo_list = models.ForeignKey(
        "app.ToDoList",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title}"
    
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)



class ToDoList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s todo list"




    # PROCESSING = 'processing'
    # COMPLETED = 'completed'
    # STATUS_BAR_LIST = [
    #     (PROCESSING, 'Processing'),
    #     (COMPLETED, 'Completed'),
    # ]

    
    # status = models.CharField(
    #     max_length=16,
    #     choices=STATUS_BAR_LIST,
    #     default=PROCESSING,
    # )