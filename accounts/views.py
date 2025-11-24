

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import LoginForm
from .models import Student
from attendance.models import AttendanceRecord
from fees.models import FeeRecord
from discipline.models import Activity, Punishment
from hostel.models import RoomAllocation
from notices.models import Notice

def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # only allow if user has Student profile
            try:
                user.student
            except Student.DoesNotExist:
                messages.error(request, "You are not registered as a student.")
                return redirect('accounts:login')

            login(request, user)
            return redirect('accounts:dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')

@login_required
def dashboard(request):
    student = Student.objects.get(user=request.user)

    attendance = AttendanceRecord.objects.filter(student=student)[:10]
    fees = FeeRecord.objects.filter(student=student)
    activities = Activity.objects.filter(student=student)[:5]
    punishments = Punishment.objects.filter(student=student)[:5]
    allocation = RoomAllocation.objects.filter(student=student).first()
    notices = Notice.objects.filter(is_active=True)[:5]

    # simple stats
    total_present = AttendanceRecord.objects.filter(student=student, status='P').count()
    total_absent = AttendanceRecord.objects.filter(student=student, status='A').count()

    context = {
        'student': student,
        'attendance': attendance,
        'fees': fees,
        'activities': activities,
        'punishments': punishments,
        'allocation': allocation,
        'notices': notices,
        'total_present': total_present,
        'total_absent': total_absent,
    }
    return render(request, 'accounts/dashboard.html', context)
