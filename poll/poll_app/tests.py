import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_recent_with_future_pub_date(self):
        future_time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_time)
        self.assertIs(future_question.recent(), False)

    def test_recent_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.recent(), False)

    def test_recent_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.recent(), True)
