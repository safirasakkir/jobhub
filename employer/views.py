from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView
from employer.forms import EmployerProfileForm,JonForm
from employer.models import EmployerProfile,Jobs,Applications
from django.urls import reverse_lazy

# Create your views here.
class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"



class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-profile.html"
    success_url = reverse_lazy("e-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
class EmployerProfileDetailView(TemplateView):
    template_name = "emp-myprofile.html"

class JobCreateView(CreateView):
    model=Jobs
    form_class = JonForm
    template_name = "emp-postjob.html"
    success_url = reverse_lazy("e-home")

    def form_valid(self, form):
        form.instance.posted_by=self.request.user
        return super().form_valid(form)

class EmployerJobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-joblist.html"

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user)

class JobDetailView(DetailView):
    model = Jobs
    template_name = "emp-jobdetail.html"
    context_object_name = "job"
    pk_url_kwarg = "id"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Applications.objects.filter(applicant=self.request.user,job=self.object)
        context['status']=qs
        return context

class ViewApplication(ListView):
    model = Applications
    template_name = 'all_applications.html'
    context_object_name = "all_app"

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get('id'))

