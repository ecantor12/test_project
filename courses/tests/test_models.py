# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from courses.models import Course
from mixer.backend.django import mixer
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime
import pytest

@pytest.mark.django_db
class TestModels:

	def test_course_is_available(self):
		start_date = make_aware(datetime.strptime("2018-01-01", "%Y-%m-%d"))
		end_date = make_aware(datetime.strptime("2018-12-12", "%Y-%m-%d"))

		course = Course.objects.create(
			name = "Course de prueba",
			start_date = start_date,
			end_date = end_date,
			description = "Descripción del curso de prueba"
			)
		assert course.is_available == True

"""
Parte 2
	def test_course_is_not_available(self):
		start_date = make_aware(datetime.strptime("2018-05-01", "%Y-%m-%d"))
		end_date = make_aware(datetime.strptime("2018-12-12", "%Y-%m-%d"))
		course = mixer.blend('courses.Course', start_date=start_date, end_date = end_date)
		assert course.is_available == False
"""