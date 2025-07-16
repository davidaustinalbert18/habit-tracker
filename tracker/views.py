from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Habit
from .forms import HabitForm
from django.utils import timezone
from .models import HabitLog
from django.shortcuts import get_object_or_404
from .models import calculate_streak
from collections import defaultdict
from datetime import timedelta, date
import json

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/signup.html', {'form': form})

@login_required
def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user # attach habit to current user
            habit.save()
            return redirect('index')
    else:
        form = HabitForm()
    return render(request, 'tracker/create_habit.html', {'form': form})

@login_required
def mark_completed(request, habit_id):
    if request.method == "POST":
        habit = get_object_or_404(Habit, id=habit_id, user=request.user)
        today = timezone.now().date()

    # Prevent duplicate logs for today
    if not HabitLog.objects.filter(habit=habit, date_completed=today).exists():
        HabitLog.objects.create(habit=habit, date_completed=today)

    return redirect('index')

@login_required
def unmark_completed(request, habit_id):
    habit = Habit.objects.get(id=habit_id, user=request.user)
    today = timezone.now().date()
    HabitLog.objects.filter(habit=habit, date_completed=today).delete()
    return redirect('index')

@login_required
def edit_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'tracker/edit_habit.html', {'form': form, 'habit': habit})


@login_required
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        habit.delete()
        return redirect('index')
    return render(request, 'tracker/delete_habit.html', {'habit': habit})

@login_required
def index(request):
    habits = Habit.objects.filter(user=request.user)
    today = date.today()

    sort = request.GET.get('sort')
    frequency = request.GET.get('frequency')

    if frequency:
        habits = habits.filter(frequency=frequency)
    print('Frequency Filter:', frequency)
    print('Matching Habits:', habits)
    for habit in habits:
        print(habit.name, '-', habit.frequency)
    
    if sort == 'name':
        habits = habits.order_by('name')
    elif sort == 'streak':
        pass
    elif sort == 'created':
        habits = habits.order_by('-id')

    past_week = [today - timedelta(days=i) for i in range(6, -1, -1)]
    habit_data = []

    for habit in habits:
        logs = habit.logs.filter(date_completed__in=past_week)
        log_dates = [log.date_completed for log in logs]
        data = []
        for day in past_week:
            data.append(1 if day in log_dates else 0)
        streak = calculate_streak(habit)
        habit_data.append({
            'habit': habit,
            'consistency': data,
            'streak': streak,
        })

    if sort == 'streak':
        habit_data.sort(key=lambda x: x['streak'], reverse=True)

    return render(request, 'tracker/index.html', {
        'habit_data': habit_data,
        'past_week': [d.strftime("%a") for d in past_week],  # e.g., ['Mon', 'Tue', ...]
        'today': today,
        'frequency': frequency,
        'sort': sort,
    })

@login_required
def stats(request):
    habits = Habit.objects.filter(user=request.user).prefetch_related('logs')
    today = timezone.now().date()

    stats_data = []

    for habit in habits:
        logs = habit.logs.order_by('-date_completed')
        total_days = (today - logs.last().date_completed).days + 1 if logs.exists() else 0
        completed_days = logs.count()

        # Completion rate calculation
        completion_rate = (completed_days / total_days * 100) if total_days > 0 else 0

        # Calculate current streak
        current_streak = calculate_streak(habit)

        stats_data.append({
            'habit': habit,
            'completed_days': completed_days,
            'total_days': total_days,
            'completion_rate': round(completion_rate),
            'current_streak': current_streak,
            'goal_total': habit.goal_total,
            'goal_met': habit.goal_total and completed_days >= habit.goal_total,
        })

    return render(request, 'tracker/stats.html', {'stats_data': stats_data})