from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'frequency', 'goal_total']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
