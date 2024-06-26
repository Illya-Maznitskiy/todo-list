from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views import View

from todo_app.forms import TaskForm
from todo_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "todo_app/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_app/task_confirm_delete.html"
    success_url = reverse_lazy("todo_app:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_app:tag-list")


class ToggleDoUndoView(View):
    def get(self, request, pk):
        return HttpResponseRedirect(reverse_lazy("todo_app:task-list"))

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.done = not task.done
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo_app:task-list"))
