from django.test import TestCase
from django.urls import resolve
from quiz.views import index
from django.http import HttpRequest
from quiz.models import Quiz

class HomePageTest(TestCase):

  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, index)

  def test_homepage_use_template(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'quiz/home.html')

class QuizModelTest(TestCase):

  def test_create_and_retrieve_question(self):
    Quiz.objects.create(question='test_question', yes_answer=True, no_answer=False)
    save_quiz = Quiz.objects.all()
    self.assertEqual(save_quiz.count(), 1)
    self.assertEqual(save_quiz[0].question, 'test_question')
    self.assertEqual(save_quiz[0].yes_answer, True)
    self.assertEqual(save_quiz[0].no_answer, False)

class QuizViewTest(TestCase):

  def test_use_start_template(self):
      response = self.client.get('/quiz/start/')
      self.assertTemplateUsed(response, 'quiz/start.html')

  def test_add_quiz(self):
      self.client.post('/', data={'question': 'test_add_quiz', 'yes_answer': True, 'no_answer': False})
      save_quiz = Quiz.objects.all()
      self.assertEqual(save_quiz.count(), 1)
      self.assertEqual(save_quiz[0].question, 'test_add_quiz')
      self.assertEqual(save_quiz[0].yes_answer, True)
      self.assertEqual(save_quiz[0].no_answer, False)

  def test_start_quiz(self):
      Quiz.objects.create(question='test_start_quiz', yes_answer=True, no_answer=False)
      response = self.client.get('/quiz/start/')
      self.assertContains(response, 'test_start_quiz')
