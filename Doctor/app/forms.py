from django import forms
import datetime

class AppointmentForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    m_number = forms.IntegerField(required=True)
    day = forms.DateField()
    time = forms.TimeField()
    addr = forms.CharField(required=True)
