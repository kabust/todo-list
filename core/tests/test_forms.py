from datetime import datetime

from django.test import TestCase

from core.forms import TaskForm, TaskSearchForm
from core.models import Tag


class TaskFormsTest(TestCase):
    def setUp(self):
        for i in range(3):
            Tag.objects.create(name=f"tag{i}")

    def test_task_form_valid(self):
        form_data = {
            "content": "Some cool task",
            "deadline": datetime.now(),
            "tags": [tag.id for tag in Tag.objects.all()]
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form_data = {
            "content": "",
            "deadline": datetime.now(),
            "tags": [tag.id for tag in Tag.objects.all()]
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_search_form_with_q_params(self):
        form_data = {
            "content": "cool"
        }
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_search_form_without_q_params(self):
        form_data = {
            "content": ""
        }
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
