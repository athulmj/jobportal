from django import forms
from employer.models import EmployerProfile,Jobs

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model=EmployerProfile
        exclude=("user",)
        widgets={
            "logo": forms.FileInput(attrs={"class": "form-control"}),
            "company_name": forms.TextInput(attrs={"class": "form-control"}),
            "bio": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "services": forms.TextInput(attrs={"class": "form-control"}),
        }

        # fields=["company_name",
        #         "logo",
        #         "bio",
        #         "location",
        #         "services"]

class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        exclude=("posted_by","created_date")
        widgets={
            "job_title": forms.TextInput(attrs={"class": "form-control"}),
            "job_description": forms.Textarea(attrs={"class": "form-control"}),
            "role": forms.TextInput(attrs={"class": "form-control"}),
            "experience": forms.NumberInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "last_date":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "qualification": forms.TextInput(attrs={"class": "form-control"})
        }