from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrganizationMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

class HomePageView(ListView):
    model = Organization
    context_object_name = "home"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        context["total_organizations"] = Organization.objects.count()
        context["total_programs"] = Program.objects.count()

        today = timezone.now().date()
        count = (
            OrgMember.objects.filter(
                date_joined__year=today.year
            )
            .values("student")
            .distinct()
            .count()
        )
        context["students_joined_this_year"] = count
        return context

class OrganizationList(ListView):
    model = Organization
    context_object_name = "organization"
    template_name = "org_list.html"
    paginate_by = 5
    ordering = ["college__college_name", "name"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query)
                )
        return qs

class OrganizationMemberListView(ListView):
    model = OrgMember
    context_object_name = "organization_member"
    template_name = "orgmem_list.html"
    paginate_by = 5
    ordering = ["student__lastname", "date_joined"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(student__lastname__icontains=query) | 
                Q(date_joined__icontains=query) 
            )
        return qs

    def get_ordering(self):
        allowed = ["student__lastname", "date_joined"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "student__lastname"

class StudentListView(ListView):
    model = Student
    context_object_name = "student"
    template_name = "student_list.html"
    paginate_by = 5

    def get_queryset(self):
            qs = super().get_queryset()
            query = self.request.GET.get("q")
            if query:
                qs = qs.filter(
                    Q(student_id__icontains=query) | 
                    Q(lastname__icontains=query) |
                    Q(firstname__icontains=query) |
                    Q(middlename__icontains=query) |
                    Q(program__prog_name__icontains=query) 
                )
            return qs

class CollegeListView(ListView):
    model = College
    context_object_name = "college"
    template_name = "college_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(college_name__icontains=query) | 
                Q(created_at__icontains=query) |
                Q(updated_at__icontains=query)
            )
        return qs

class ProgramListView(ListView):
    model = Program
    context_object_name = "program"
    template_name = "program_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(prog_name__icontains=query) | 
                Q(college__college_name__icontains=query) 
            )
        return qs
    
    def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
       
        if sort_by in allowed:
           return sort_by
        return "prog_name"

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")

class OrganizationMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrganizationMemberForm
    template_name = "orgmem_form.html"
    success_url = reverse_lazy("organization-member-list")

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "stu_form.html"
    success_url = reverse_lazy("student-list")


class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")


class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "prog_form.html"
    success_url = reverse_lazy("program-list")

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")

class OrganizationMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrganizationMemberForm
    template_name = "orgmem_form.html"
    success_url = reverse_lazy("organization-member-list")

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "stu_form.html"
    success_url = reverse_lazy("student-list")


class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")


class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "prog_form.html"
    success_url = reverse_lazy("program-list")

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "org_del.html"
    success_url = reverse_lazy("organization-list")

class OrganizationMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = "orgmem_del.html"
    success_url = reverse_lazy("organization-member-list")

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "stu_del.html"
    success_url = reverse_lazy("student-list")

class CollegeDeleteView(DeleteView):
    model = College
    template_name = "college_del.html"
    success_url = reverse_lazy("college-list")

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "prog_del.html"
    success_url = reverse_lazy("program-list")