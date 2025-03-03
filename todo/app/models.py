from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=255)
    todo_list = models.ForeignKey(
        "app.ToDolist", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Task {self.title}"
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class ToDoList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return f"{self.user.username}'s tasks"



# from django.db import models
# from django.contrib.auth.models import User


# class Task(models.Model):
#     title = models.CharField(max_length=255)
#     todo_list = models.ForeignKey(
#         "app.ToDoList",
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )

#     def __str__(self):
#         return f"Task {self.title}"
    
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)



# class ToDoList(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     label = models.CharField(max_length=32, null=True, blank=True)

#     def __str__(self):
#         return f"{self.user.username}'s todo list"




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