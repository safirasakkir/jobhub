from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from candidate.forms import CandidateProfileForm
from django.views.generic import TemplateView,CreateView,DetailView,ListView
from candidate.models import CandidateProfile
from employer.models import Jobs,Applications
# Create your views here.


class CandidateHomeView(TemplateView):
    template_name = "cand-home.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Jobs.objects.all()
        context["jobs"]=qs
        return context


class CandidateProfileCreateView(CreateView):
    model=CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-profile.html"
    success_url = reverse_lazy("cand-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class CandidateJobDetailView(DetailView):
    template_name = "cand-detailjob.html"
    model=Jobs
    context_object_name = "job"
    pk_url_kwarg = "id"

def apply_now(request,*args,**kwargs):
    job_id=kwargs.get('id')
    job=Jobs.objects.get(id=job_id)
    applicant=request.user
    Applications.objects.create(applicant=applicant,job=job)
    return redirect("cand-home")

class MyApplicationView(ListView):
    model = Applications
    template_name = "applied_jobs.html"
    context_object_name = 'applied'

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)