from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from core.forms import TaskForm, TaskSearchForm
from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task

    def get_queryset(self):
        queryset = Task.objects.prefetch_related("tags")
        params = self.request.GET.get("content")

        if params:
            queryset = queryset.filter(content__icontains=params)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        content = self.request.GET.get("content", "")
        context["form"] = TaskSearchForm(initial={"content": content})
        return context


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("core:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("core:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("core:index")


def toggle_complete_todo(
        request: HttpRequest,
        pk: int
) -> HttpResponseRedirect:
    task = get_object_or_404(Task, pk=pk)

    task.is_done = not task.is_done
    task.save()

    return HttpResponseRedirect(reverse("core:index"))


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("core:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("core:tag-list")
