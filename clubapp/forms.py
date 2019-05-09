from django import forms
from .models import Meeting, MeetingMinutes, Resource, Event

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'