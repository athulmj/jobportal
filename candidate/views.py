from django.shortcuts import render,redirect
from candidate.forms import CandidateProfileForm
from django.views.generic import TemplateView,CreateView,DetailView,ListView,UpdateView
from candidate.models import CandidateProfile
from django.urls import reverse_lazy
from employer.models import Jobs,Applications
from candidate.filters import JobFilter
from django.utils.decorators import method_decorator
from users.decorators import signin_required
from django.contrib import messages


@method_decorator(signin_required,name="dispatch")
class CandidateHomeView(ListView):
    model = Jobs
    paginate_by = 2
    template_name = "cand-home.html"


    def get(self, request, *args, **kwargs):
        filter = JobFilter(request.GET, queryset=Jobs.objects.all())
        return render(request, "cand-home.html", {"filter": filter})

    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     qs=Jobs.objects.all()
    #     context["jobs"]=qs
    #     return context

@method_decorator(signin_required,name="dispatch")
class CandidateProfileCreateView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-profile.html"
    success_url = reverse_lazy("cand-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

@method_decorator(signin_required,name="dispatch")
class CandidateProfileDetailView(TemplateView):
    template_name = "cand-myprofile.html"

@method_decorator(signin_required,name="dispatch")
class CandidateProfileEditView(UpdateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-editprofile.html"
    success_url = reverse_lazy("cand-home")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request,'Profile has been updated')
        return super().form_valid(form)

@method_decorator(signin_required,name="dispatch")
class CandidateJobDetailView(DetailView):
    model = Jobs
    template_name = "cand-detailjob.html"
    context_object_name = "job"
    pk_url_kwarg = "id"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Applications.objects.filter(applicant=self.request.user,job=self.object)
        context['status']=qs
        return context

@signin_required
def apply_now(request,*args,**kwargs):
    job_id=kwargs.get("id")
    job=Jobs.objects.get(id=job_id)
    applicant=request.user
    Applications.objects.create(applicant=applicant,job=job)
    return redirect("cand-home")

@method_decorator(signin_required,name="dispatch")
class MyApplicationView(ListView):
    model = Applications
    template_name = "cand-appliedjoblist.html"
    context_object_name = "applied"

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)

@method_decorator(signin_required,name="dispatch")
class AcceptedApplicationsView(ListView):
    model = Applications
    template_name = "cand-acceptedjob.html"
    context_object_name = 'application'

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user,status='accepted')