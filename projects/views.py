from django.shortcuts import render
from projects.models import Project


def project_home(request):
    projects = Project.objects.all()
    data = {
        'projects': projects,
    }
    return render(request, 'projects/project_home.html', data)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    data = {
        'project': project,
    }
    return render(request, 'projects/project_detail.html', data)
