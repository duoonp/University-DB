#import pdb;
#from django.shortcuts import redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from students.forms import *
from students.models import *

def main_page(request):
    return render_to_response(
      'main_page.html', RequestContext(request)
    )
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
#-----------------------
@login_required
def student_add(request, group_title=None):
    if group_title:
            group = get_object_or_404(Group, title=group_title)
    else:
        group = None
            
    if request.method == 'POST':
        form = StudentAddForm(request.POST, initial={'group': group})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = StudentAddForm(initial={'group': group})
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('student_add.html', variables)

@login_required
def group_add(request):
    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = GroupAddForm(initial={})
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response('group_add.html', variables)

        
@login_required
def delete_data(request,  instance, instance_id):
    if instance == "student":
        student_id = instance_id
        student = get_object_or_404(Student, id=student_id)
        student.delete()
    else:
        group_id = instance_id
        group = get_object_or_404(Group, id=group_id)
        group.delete()
    return HttpResponseRedirect('/')

def students_list(request, group_title=None):
    if group_title:
        group = get_object_or_404(Group, title=group_title)
        students = Student.objects.filter(group=group)
        variables = RequestContext(request, {
            'students': students,
            'group_title': group_title
        })
        return render_to_response('students_group_list.html', variables)
    else:
        students = Student.objects.order_by('name')
        variables = RequestContext(request, {
            'students': students,
        })
        return render_to_response('students_all_list.html', variables)

def groups_list(request):
    groups = Group.objects.order_by('title')
    variables = RequestContext(request, {
        'groups': groups,
    })
    return render_to_response('all_groups_list.html', variables)

def edit_data(request,  instance, instance_id):
    if instance == "student":
        student_id = instance_id
        student = get_object_or_404(Student, id=student_id)
        
        if request.method == 'POST':
            form = StudentAddForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = StudentAddForm(instance=student)
            variables = RequestContext(request, {
                'form': form
                            })
            return render_to_response('student_add.html', variables)
        
    elif instance == 'group':
        group_id = instance_id
        group = get_object_or_404(Group, id=group_id)
        
        if request.method == 'POST':
            form = GroupAddForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = GroupAddForm(instance=group)
            variables = RequestContext(request, {
                'form': form
                             })
            return render_to_response('group_add.html', variables)

class DataUpdate(FormView):
    form_class = StudentAddForm
    model = Student
    template_name = 'student_add.html'
    success_url = '/'

    
