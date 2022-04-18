from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('find', views.find, name='find'),
    path('add_task', views.add_new_task, name='add_task')
]
