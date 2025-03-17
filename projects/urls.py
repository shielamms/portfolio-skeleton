from django.urls import path
from projects import views

urlpatterns = [
    path("", views.project_home, name="project_home"),
    path("<int:pk>/", views.project_detail, name="project_detail")
]
