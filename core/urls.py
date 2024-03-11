from django.urls import path

from core.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_complete_todo,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("new-todo/", TaskCreateView.as_view(), name="todo-create"),
    path(
        "update-todo/<int:pk>/", TaskUpdateView.as_view(), name="todo-update"
    ),
    path(
        "delete-todo/<int:pk>/", TaskDeleteView.as_view(), name="todo-delete"
    ),
    path(
        "<int:pk>/toggle-complete/",
        toggle_complete_todo,
        name="toggle-complete"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/add/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "core"
