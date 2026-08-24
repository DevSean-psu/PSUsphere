from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from studentorg.models import Organization


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