# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Course
from django.shortcuts import render

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'object_list': courses})

def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except:
        course = None
    return render(request, 'courses/course_detail.html', {'course': course})

"""
class CourseList(ListView):
    model = Course

class CourseDetail(DetailView):
    model = Course
"""

class CourseCreation(CreateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'start_date', 'end_date', 'description']

class CourseUpdate(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'start_date', 'end_date', 'description']

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
