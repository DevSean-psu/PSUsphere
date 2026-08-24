from django.views.generic import ListView
from studentorg.models import Organization, College, Program, Student


class HomePageView(ListView):
    model = Organization
    context_object_name = 'organizations'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['organization_count'] = Organization.objects.count()
        context['college_count'] = College.objects.count()
        context['program_count'] = Program.objects.count()
        context['student_count'] = Student.objects.count()

        return context