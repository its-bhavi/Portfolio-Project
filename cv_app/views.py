from django.shortcuts import render, redirect, get_object_or_404
from .models import CV, Contact, Education, WorkExperience, Skill, Certificate, Project, SocialLink
from .forms import ContactForm, EducationForm, WorkExperienceForm, SkillForm, CertificateForm, ProjectForm, SocialLinkForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm  # Ensure your form is imported
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Cache for 15 minutes
def profile_view(request):
    # your view code heredef profile_view(request):
    contact = request.user.cv.contacts.select_related("cv").first()  # Optimize fetching
    # Your existing code
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'cv_app/profile.html', {'form': form, 'contact': contact})
    ...


def projects_view(request):
    query = request.GET.get('q')
    if query:
        projects = request.user.cv.projects.filter(title__icontains=query)
    else:
        projects = request.user.cv.projects.all()

    return render(request, 'cv_app/projects.html', {'projects': projects})

def add_project_view(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.cv = request.user.cv
            project.save()
            messages.success(request, "Project added successfully!")
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'cv_app/add_project.html', {'form': form})

def edit_project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id, cv=request.user.cv)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully!")
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'cv_app/edit_project.html', {'form': form})

def delete_project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id, cv=request.user.cv)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted successfully!")
        return redirect('projects')
    return render(request, 'cv_app/confirm_delete.html', {'item': project})


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create CV instance for the new user
            CV.objects.create(user=user)
            login(request, user)  # Automatically log in the user after registration
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('cv_home')  # Redirect to home or a welcome page
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def cv_home(request):
    return render(request, 'cv_app/cv_home.html')



def contact_view(request):
    contact, created = Contact.objects.get_or_create(cv=request.user.cv)
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)  # Ensure FILES is included
        if form.is_valid():
            form.save()
            messages.success(request, "Contact information saved successfully!")
            return redirect('cv_home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'cv_app/contact.html', {'form': form})


def education_view(request):
    educations = request.user.cv.education.all()
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.cv = request.user.cv
            education.save()
            return redirect('education')
    else:
        form = EducationForm()
    return render(request, 'cv_app/education.html', {'form': form, 'educations': educations})

def edit_education(request, education_id):
    education = get_object_or_404(Education, id=education_id, cv=request.user.cv)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, "Education details updated successfully!")
            return redirect('education')
    else:
        form = EducationForm(instance=education)
    return render(request, 'cv_app/edit_education.html', {'form': form})

def delete_education(request, education_id):
    education = get_object_or_404(Education, id=education_id, cv=request.user.cv)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Education details deleted successfully!")
        return redirect('education')
    return render(request, 'cv_app/confirm_delete.html', {'item': education})

def work_experience_view(request):
    experiences = request.user.cv.work_experience.all()
    if request.method == "POST":
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.cv = request.user.cv
            experience.save()
            return redirect('work_experience')
    else:
        form = WorkExperienceForm()
    return render(request, 'cv_app/work_experience.html', {'form': form, 'experiences': experiences})

def skills_view(request):
    if not hasattr(request.user, 'cv'):
        CV.objects.create(user=request.user)  # Create if no CV exists

    skills = request.user.cv.skills.all()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.cv = request.user.cv
            skill.save()
            return redirect('skills')
    else:
        form = SkillForm()

    return render(request, 'cv_app/skills.html', {'form': form, 'skills': skills})

def certificates_view(request):
    certificates = request.user.cv.certificates.all()
    if request.method == "POST":
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.cv = request.user.cv
            certificate.save()
            return redirect('certificates')
    else:
        form = CertificateForm()
    return render(request, 'cv_app/certificates.html', {'form': form, 'certificates': certificates})



def social_links_view(request):
    social_links = request.user.cv.social_links.all()
    if request.method == "POST":
        form = SocialLinkForm(request.POST)
        if form.is_valid():
            social_link = form.save(commit=False)
            social_link.cv = request.user.cv
            social_link.save()
            return redirect('social_links')
    else:
        form = SocialLinkForm()
    return render(request, 'cv_app/social_links.html', {'form': form, 'social_links': social_links})

def project_detail_view(request, project_id):
    project = get_object_or_404(Project, id=project_id, cv=request.user.cv)
    return render(request, 'cv_app/project_detail.html', {'project': project})




def update_profile_view(request):
    contact = request.user.cv.contacts.first()  # Assuming one contact exists
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'cv_app/update_profile.html', {'form': form})

def base_view(request):
    return render(request, 'cv_app/base.html')  # Ensure you have a base.html template