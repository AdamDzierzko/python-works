import json

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Task


def index(request: HttpRequest) -> HttpResponse:
    """
    Sends all tasks into index.html page.

    :param HttpRequest request: HttpRequest from index.
    :return HttpResponse render: HttpResponse to index.html
    """
    tasks = Task.objects.all()

    return render(request, "TODO_works/index.html", {
        "tasks": tasks
    })


@csrf_exempt
def add_new_task(request: HttpRequest) -> HttpResponse:
    """
    Adds new task to DB.
    Data is passed via addtask function in index.js, which sends data by post method.

    :param HttpRequest request: HttpRequest from index.
    :return: redirect to main page
    """

    data = json.loads(request.body)

    task = Task()
    task.opis = data.get("description", "")
    task.save()

    return JsonResponse({"message": "OK"}, status=201)


def delete_task(request: HttpRequest, task_id: int) -> HttpResponseRedirect:
    """
    Removes selected task from DB.

    :param HttpRequest request: HttpRequest from index.
    :param int task_id: Primary Key to select proper task from DB
    :return: redirect to main page
    """
    task = Task.objects.get(pk=task_id)
    task.delete()

    return HttpResponseRedirect(reverse("index"))


@csrf_exempt
def find(request: HttpRequest) -> HttpResponse:
    """
    Finds tasks that contain the searched phrase in the description.
    Data is passed by post method from html form.

    :param HttpRequest request: HttpRequest from index.
    :return HttpResponse render: HttpResponse to index.html
    """
    if request.method == "POST":
        phrase = request.POST.get("find_task")
        all_tasks = Task.objects.all()
        tasks = []

        for single_task in all_tasks:
            if phrase in single_task.opis:
                tasks.append(single_task)

        return render(request, "TODO_works/index.html", {
            "tasks": tasks
        })
    else:
        return HttpResponseRedirect(reverse("index"))
