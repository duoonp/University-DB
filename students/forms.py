from django.forms import ModelForm
from students.models import Student, Group

class StudentAddForm(ModelForm):
    class Meta:
        model = Student

class GroupAddForm(ModelForm):
    class Meta:
        model = Group