from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_home, name='cv_home'),
    path('contact/', views.contact_view, name='contact'),
    path('education/', views.education_view, name='education'),
    path('work_experience/', views.work_experience_view, name='work_experience'),
    path('skills/', views.skills_view, name='skills'),
    path('certificates/', views.certificates_view, name='certificates'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/add/', views.add_project_view, name='add_project'),
    path('projects/edit/<int:project_id>/', views.edit_project_view, name='edit_project'),
    path('projects/delete/<int:project_id>/', views.delete_project_view, name='delete_project'),
    path('social_links/', views.social_links_view, name='social_links'),
    path('education/edit/<int:education_id>/', views.edit_education, name='edit_education'),
    path('education/delete/<int:education_id>/', views.delete_education, name='delete_education'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.update_profile_view, name='update_profile'),
    path('base/', views.base_view, name='base'),  # Now, /base will work
]