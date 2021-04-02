from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# list and create -pk not reqiured
class StudentList(ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


class StudentChange(RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

	