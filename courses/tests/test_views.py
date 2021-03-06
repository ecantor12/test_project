from django.test import RequestFactory
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from courses.views import *
from mixer.backend.django import mixer
from django.test import TestCase
import pytest




#Parte1
@pytest.mark.django_db
class TestViews:

	def test_course_list_authenticated(self):
		path = reverse('courses:list')
		request = RequestFactory().get(path)
		request.user = mixer.blend(User)

		response = course_list(request)
		assert response.status_code == 200

	def test_course_list_unauthenticated(self):
		path = reverse('courses:list')
		request = RequestFactory().get(path)
		request.user = AnonymousUser()

		response = course_list(request)
		assert 'accounts/login' in response.url

	def test_course_detail_without_object_course(self):
		c = Client()
		path = reverse('courses:detail', args=[1])
		response = c.get(path)
		assert 'No hay datos para mostrar' in response.content

	def test_course_delete_without_object_course(self):
		c = Client()
		path = reverse('courses:delete', args=[1])
		response = c.get(path)
		assert response.status_code == 404

	def test_course_delete_object_course_confirm_message(self):
		course = mixer.blend('courses.Course', pk=1, name='prueba')
		c = Client()
		path = reverse('courses:delete', args=[1])
		response = c.get(path)
		message = 'seguro que deseas borrar el curso '+ '"'+course.name+'"'
		url = 'courses/borrar/'+str(course.pk)
		assert  message in response.content
		assert  url in response.request['PATH_INFO']

	def test_course_delete_object_course(self):
		mixer.blend('courses.Course', pk=1)
		c = Client()
		path = reverse('courses:delete', args=[1])
		response = c.post(path)
		assert 'courses' in response.url
		assert response.status_code == 302



"""
#Parte 2
@pytest.fixture
def factory(db):
	return RequestFactory()

@pytest.fixture
def course(db):
	return mixer.blend('courses.Course', pk=1, name='prueba')

@pytest.fixture
def client(db):
	return Client()

def test_course_list_authenticated(factory):
	path = reverse('courses:list')
	request = factory.get(path)
	request.user = mixer.blend(User)
	response = course_list(request)
	assert response.status_code == 200

def test_course_list_unauthenticated(factory):
	path = reverse('courses:list')
	request = factory.get(path)
	request.user = AnonymousUser()
	response = course_list(request)
	assert 'accounts/login' in response.url

def test_course_detail_without_object_course(client):
	path = reverse('courses:detail', args=[1])
	response = client.get(path)
	assert 'No hay datos para mostrar' in response.content

def test_course_delete_without_object_course(client):
	path = reverse('courses:delete', args=[1])
	response = client.get(path)
	assert response.status_code == 404

def test_course_delete_object_course_confirm_message(client, course):
	path = reverse('courses:delete', args=[1])
	response = client.get(path)
	message = 'seguro que deseas borrar el curso '+ '"'+course.name+'"'
	url = 'courses/borrar/'+str(course.pk)
	assert  message in response.content
	assert  url in response.request['PATH_INFO']

def test_course_delete_object_course(client, course):
	path = reverse('courses:delete', args=[1])
	response = client.post(path)
	assert 'courses' in response.url
	assert response.status_code == 302
"""

