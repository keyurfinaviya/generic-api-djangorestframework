
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Student/', views.StudentList.as_view()),
    path('Student/<int:pk>/', views.StudentChange.as_view()),
   

]
