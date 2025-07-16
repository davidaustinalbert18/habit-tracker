from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=50, choices=[
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ], default='Daily')
    created_at = models.DateTimeField(auto_now_add=True)
    goal_total = models.PositiveIntegerField(null=True, blank=True, help_text="Optional total completions goal")

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='logs')
    date_completed = models.DateField()

    def __str__(self):
        return f"{self.habit.name} on {self.date_completed}"
    
def calculate_streak(habit):
    logs = habit.logs.order_by('-date_completed')
    today = timezone.now().date()

    streak = 0
    expected_date = today

    for log in logs:
        if log.date_completed == expected_date:
            streak += 1
            expected_date -= timedelta(days=1)
        elif log.date_completed < expected_date:
            break  # streak is broken

    return streak
