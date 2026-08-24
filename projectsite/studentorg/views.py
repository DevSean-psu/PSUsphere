from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from studentorg.models import Organization, Student, Program, College


class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'


class OrganizationListView(ListView):
    model = Organization
    context_object_name = 'organizations'
    template_name = 'organizations.html'


class OrganizationDetailView(DetailView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'organization_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['members'] = self.object.orgmember_set.select_related(
            'student',
            'student__program'
        ).all()

        return context


class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students.html'
    paginate_by = 20


class ProgramListView(ListView):
    model = Program
    context_object_name = 'programs'
    template_name = 'programs.html'
    paginate_by = 20


class CollegeListView(ListView):
    model = College
    context_object_name = 'colleges'
    template_name = 'colleges.html'
    paginate_by = 20