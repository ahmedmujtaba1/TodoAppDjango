from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('task/<int:task_id>/',views.display_task,name="index"),
    path('save_task/', views.save_task, name="save_task"),
    path('mark_complete/<int:task_id>/',views.mark_complete,name="mark_complete"),
    path('delete_task/<int:task_id>/',views.delete_task,name="delete_task"),
    path('edit_task/<int:task_id>/', views.edit_task_view, name='edit_task'),
]
