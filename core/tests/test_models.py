from datetime import datetime
import pytz

from django.test import TestCase

from core.models import Tag, Task


class TagModelTest(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="cool_tag")
        self.assertEqual(str(tag), tag.name)


class TaskModelTest(TestCase):
    def setUp(self):
        utc = pytz.UTC
        self.task = Task.objects.create(
            content="cool task",
            deadline=utc.localize(
                datetime(2024, 3, 1, 12, 30)
            )
        )

    def test_task_str(self):
        self.assertEqual(str(self.task), self.task.content)

    def test_task_is_past_deadline(self):
        self.assertTrue(self.task.is_past_deadline())

    def test_task_is_not_past_deadline(self):
        utc = pytz.UTC
        self.task.deadline = utc.localize(
                datetime(2029, 10, 1, 12, 30)
            )

        self.assertFalse(self.task.is_past_deadline())
