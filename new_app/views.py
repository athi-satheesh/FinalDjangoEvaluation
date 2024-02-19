from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from new_app.forms import RegistrationForm, studentRegistrationForm, adminRegistrationForm, MarksForm
from new_app.models import Student, Marks


# Create your views here.
def base(request):
    return render(request, "index.html")


def admin_register(request):
    reg_form = RegistrationForm()
    admin_reg_form = adminRegistrationForm()
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        admin_reg_form = adminRegistrationForm(request.POST, request.FILES)
        if reg_form.is_valid() and admin_reg_form.is_valid():
            admin_reg = reg_form.save(commit=False)
            admin_reg.is_admin = True
            admin_reg.save()
            reg = admin_reg_form.save(commit=False)
            reg.user = admin_reg
            reg.save()
            return redirect('login1')
    return render(request, "admin_RegistrationForm.html", {'reg_form': reg_form, 'admin_form': admin_reg_form})


def student_register(request):
    reg_form = RegistrationForm()
    stud_reg_form = studentRegistrationForm()
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        stud_reg_form = studentRegistrationForm(request.POST, request.FILES)
        if reg_form.is_valid() and stud_reg_form.is_valid():
            stud_reg = reg_form.save(commit=False)
            stud_reg.is_student = True
            stud_reg.save()
            reg = stud_reg_form.save(commit=False)
            reg.user = stud_reg
            reg.save()
            return redirect('login1')
    return render(request, "student_RegistrationForm.html", {'reg_form': reg_form, 'stud_form': stud_reg_form})


def admin_login(request):
    return render(request, "admin_index.html")


def student_login(request):
    return render(request, "student_index.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_admin:
                print("HII")
                return redirect('adminLogin')
            elif user.is_student:
                return redirect('studentLogin')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, "Login.html")


def add_marks(request):
    addMark_form = MarksForm()
    if request.method == 'POST':
        addMark_form = MarksForm(request.POST)
        if addMark_form.is_valid():
            addMark_form1 = addMark_form.save(commit=False)
            addMark_form1.save()
            return redirect('viewMarks')
    return render(request, "addmarks.html", {'addMark_form': addMark_form})


def viewMarksbyAdmin(request):
    data1 = Marks.objects.all()
    return render(request, "viewMarksByadmin.html", {'data1': data1})


def updateMarks(request, id):
    mark_data = Marks.objects.get(id=id)
    mark_form = MarksForm(instance=mark_data)
    if request.method == "POST":
        mark_form1 = MarksForm(request.POST, instance=mark_data)
        if mark_form1.is_valid():
            mark_form1.save()
            return redirect('viewMarks')
    return render(request, "editMarkList.html", {'mark_form': mark_form})


def viewStudentList(request):
    data = Student.objects.all()
    return render(request, "admin_viewStudentList.html", {'data': data})


def viewInfo(request):
    user = request.user
    data = Student.objects.get(user=user)
    return render(request, "stud_viewinfo.html", {'data': data})

def updateInfo(request, id):
    stud_data = Student.objects.get(id=id)
    stud_form = studentRegistrationForm(instance=stud_data)
    if request.method == "POST":
        stud_form1 = studentRegistrationForm(request.POST, instance=stud_data)
        if stud_form1.is_valid():
            stud_form1.save()
            return redirect('viewInfo')
    return render(request, "updateInfo.html", {'stud_form': stud_form})


#api_views
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from new_app.models import Student
from new_app.serializer import Student_listSerializer


@api_view(['GET', 'POST'])
def studentDetails(request):
    if request.method == "GET":
        details = Student.objects.all()
        serializer = Student_listSerializer(details, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = Student_listSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_detail(request, id):
    try:
        std = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = Student_listSerializer(std)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Student_listSerializer(std, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        std.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_204_NO_CONTENT)