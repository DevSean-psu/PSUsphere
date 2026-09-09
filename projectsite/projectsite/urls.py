"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

from studentorg import views


urlpatterns = [

    path("admin/", admin.site.urls),

    # Allauth routes
    path("accounts/", include("allauth.urls")),

    path("", views.HomePageView.as_view(), name="home"),

    path("organization_list", views.OrganizationList.as_view(), name="org_list"),
    path("organization_list/add", views.OrganizationCreateView.as_view(), name="org_add"),
    path("organization_list/<pk>", views.OrganizationUpdateView.as_view(), name="org_update"),
    path("organization_list/<pk>/delete", views.OrganizationDeleteView.as_view(), name="org_delete"),

    path("orgmem_list", views.OrganizationMemberListView.as_view(), name="orgmember_list"),
    path("orgmem_list/add", views.OrganizationMemberCreateView.as_view(), name="orgmember_add"),
    path("orgmem_list/<pk>", views.OrganizationMemberUpdateView.as_view(), name="orgmember_update"),
    path("orgmem_list/<pk>/delete", views.OrganizationMemberDeleteView.as_view(), name="orgmember_delete"),

    path("student_list", views.StudentListView.as_view(), name="student_list"),
    path("student_list/add", views.StudentCreateView.as_view(), name="student_add"),
    path("student_list/<pk>", views.StudentUpdateView.as_view(), name="student_update"),
    path("student_list/<pk>/delete", views.StudentDeleteView.as_view(), name="student_delete"),

    path("college_list", views.CollegeListView.as_view(), name="college_list"),
    path("college_list/add", views.CollegeCreateView.as_view(), name="college_add"),
    path("college_list/<pk>", views.CollegeUpdateView.as_view(), name="college_update"),
    path("college_list/<pk>/delete", views.CollegeDeleteView.as_view(), name="college_delete"),

    path("program_list", views.ProgramListView.as_view(), name="program_list"),
    path("program_list/add", views.ProgramCreateView.as_view(), name="program_add"),
    path("program_list/<pk>", views.ProgramUpdateView.as_view(), name="program_update"),
    path("program_list/<pk>/delete", views.ProgramDeleteView.as_view(), name="program_delete"),

]