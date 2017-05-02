# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from itertools import count

from django.contrib import messages
from django.template import loader
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from todo.models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}

    return render(request, 'todo/index.html', context)


def add(request):
    if (request.method == "POST"):
        form = TodoForm(request.POST)


        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']

            todo = Todo()

            todo.title = title
            todo.text = text

            todo.save()
            messages.success(request, 'The todo "' + todo.title + '" has been successfully created!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'The form is not valid. Please fill the inputs correctly.')
    else:
        form = TodoForm()
        context = {'form': form}

        return render(request, 'todo/add.html', context)


def detail(request, id):
    todo = Todo.objects.get(pk=id)
    context = {'todo': todo}

    return render(request, 'todo/details.html', context)


def delete(request, id):
    if (request.method == "POST"):
        todo = Todo.objects.get(pk=id)
        messages.error(request, 'The todo has been successfully deleted')
        todo.delete()
        return redirect('/')


def edit(request, id):
    todo = Todo.objects.get(pk=id)

    if (request.method == "POST"):
        form = TodoForm(request.POST)
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.text = form.cleaned_data['text']
            todo.save()
            messages.success(request, 'The todo "' + todo.title + '" has been successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'The form is not valid. Please fill the inputs correctly.')

    else:
        form = TodoForm({
            'text': todo.text,
            'title': todo.title
        })

        context = {'todo': todo, 'form': form }

    return render(request, 'todo/edit.html', context)