from django.test import TestCase
from django.urls import reverse

from core.models import Task, Tag


class TaskListViewTest(TestCase):
    def setUp(self):
        number_of_tasks = 10

        for pk in range(1, number_of_tasks + 1):
            Tag.objects.create(name=f"Tag {pk}")
            task = Task.objects.create(
                content=f"Task {pk}",
            )
            task.tags.set([pk])

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse("core:index"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("core:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/task_list.html')

    def test_list_all_tasks(self):
        response = self.client.get(reverse("core:index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["task_list"]), 10)


class TestTaskCreateView(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Cool tag")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse("core:todo-create"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("core:todo-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/task_form.html')

    def test_view_creates_an_instance(self):
        self.client.post(
            reverse("core:todo-create"),
            data={"content": "Testing.."}
        )


class TestTaskCompleteToggle(TestCase):
    def test_task_toggle_redirects_to_home_page(self):
        task = Task.objects.create(content="Testing..")
        response = self.client.get(
            reverse("core:toggle-complete",
                    kwargs={"pk": task.id})
        )
        self.assertEqual(response.status_code, 302)

    def test_task_toggle_changes_attribute(self):
        task = Task.objects.create(content="Testing..")
        self.assertFalse(task.is_done)
        self.client.get(reverse("core:toggle-complete", args=(task.id,)))
        self.assertTrue(Task.objects.last().is_done)
