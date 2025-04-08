from django import forms
from .models import Contact, Education, WorkExperience, Skill, Certificate, Project, SocialLink
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['phone_number', 'email', 'address', 'profile_image']  # Include profile_image

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isnumeric() or len(phone_number) < 10:
            raise ValidationError("Enter a valid phone number.")
        return phone_number


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'year_started', 'year_completed']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['position', 'company', 'start_year', 'end_year', 'description']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'description', 'link']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link']

class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['platform', 'url']