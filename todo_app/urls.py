from django.urls import path

from todo_app.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    ToggleDoUndoView,
)


app_name = "todo_app"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path(
        "create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        'tasks/<int:pk>/update/',
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        'tasks/<int:pk>/delete/',
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path("<int:pk>/toggle/", ToggleDoUndoView.as_view(), name="toggle-task"),
    path("tags", TagListView.as_view(), name="tag-list"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create"
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]
