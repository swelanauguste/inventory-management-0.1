from django import forms
from django.forms import DateInput, HiddenInput, Select

from .models import ComputerAssignment, Supplier


class ComputerUnAssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = ComputerAssignment
        fields = "__all__"
        widgets = {
            "computer": Select(
                attrs={"class": "visually-hidden-focusable"},
            ),
            "employee": HiddenInput(),
            "date_assigned": HiddenInput(),
        }
        labels = {
            "computer": "",
        }


class ComputerAssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = ComputerAssignment
        fields = "__all__"
        exclude = ["date_returned"]
        widgets = {
            "computer": HiddenInput(),
        }
        labels = {
            "computer": "",
        }
