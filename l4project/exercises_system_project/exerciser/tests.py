from django.test import TestCase, Client
from exerciser.models import Application, User, Teacher, Step, Group, AcademicYear, Student
from django.utils import timezone
from django.core.urlresolvers import reverse


#imports for views
from django.core.urlresolvers import reverse

# models test
class ApplicationTest(TestCase):

	def test_application_creation(self):
		app = Application.objects.get_or_create(name = 'test app')[0]
		self.assertTrue(isinstance(app, Application))
		self.assertEqual(app.__unicode__(), app.name)
		
		
class IndexViewTests(TestCase):

	def test_index_view_with_no_applications(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['applications'], [])
		
	def test_index_view_with_applications(self):
		response = self.client.get(reverse('index'))
		app = Application.objects.get_or_create(name = 'test app')[0]
		self.assertEqual(response.status_code, 200)
		self.assertEqual((response.context['applications'] >= 0), True)

		
class LogInfoDbTests(TestCase):
	def setUp(self):
			# Setup Test User
			user = User.objects.create_user(
				username='test user',
				password='password'
			)
			teacher = Teacher.objects.get_or_create(user = user)[0]
			app = Application.objects.get_or_create(name = 'test app')[0]
			step = Step.objects.get_or_create(application = app, order = 1)[0]
		



	def test_log_info_db_valid(self):
		c = Client()
		"""
		c.login(username='test user',password='password)
		engine = import_module(settings.SESSION_ENGINE)
		store = engine.SessionStore()
		store.save()  # we need to make load() work, or the cookie isworthless
		c.cookies[settings.SESSION_COOKIE_NAME] = store.session_key
		session = c.session
		session.update({'time': 20, 'step':1,'direction':'next',example_name:'test app'})
		session.save()
		"""
		
		response = c.post(reverse('log_info_db'), {'time': 20, 'step': 1, 'direction' : 'next', 'example_name':'test app'})
		self.assertEqual(response.status_code, 200)
