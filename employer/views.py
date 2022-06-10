from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView
from employer.forms import EmployerProfileForm,JobForm
from employer.models import EmployerProfile,Jobs,Applications
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from users.decorators import signin_required
from django.contrib import messages

@method_decorator(signin_required,name="dispatch")
class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"

@method_decorator(signin_required,name="dispatch")
class EmployerProfileCreateView(CreateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-profile.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form=EmployerProfileForm(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         profile=form.save(commit=False)
    #         profile.user=request.user
    #         profile.save()
    #         print("Profile Created")
    #         return redirect("emp-home")
    #     else:
    #         return render(request,self.template_name,{"form":form})

@method_decorator(signin_required,name="dispatch")
class EmployeeProfileDetailView(TemplateView):
    template_name = "emp-myprofile.html"

@method_decorator(signin_required,name="dispatch")
class EmployerProfileEditView(UpdateView):
    model = EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-editprofile.html"
    success_url = reverse_lazy("emp-home")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request,'Profile has been updated')
        return super().form_valid(form)

@method_decorator(signin_required,name="dispatch")
class JobCreateView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-postjob.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.posted_by=self.request.user
        messages.success(self.request,"Job has been posted successfully")
        return super().form_valid(form)

@method_decorator(signin_required,name="dispatch")
class EmployerJobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-joblist.html"
    paginate_by = 3

    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user).order_by("-created_date")

@method_decorator(signin_required,name="dispatch")
class JobDetailView(DetailView):
    model = Jobs
    template_name = "emp-jobdetail.html"
    context_object_name = "job"
    pk_url_kwarg = "id"

@method_decorator(signin_required,name="dispatch")
class JobEditView(UpdateView):
    model=Jobs
    form_class = JobForm
    template_name = "emp-jobedit.html"
    success_url = reverse_lazy("emp-home")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request,'Job has been updated')
        return super().form_valid(form)


@method_decorator(signin_required,name="dispatch")
class ViewApplicationView(ListView):
    model = Applications
    template_name = "emp-candapps.html"
    context_object_name = "all_app"

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get('id'),status='applied')

@method_decorator(signin_required,name="dispatch")
class ApplicantDetailView(DetailView):
    model = Applications
    template_name = "emp-applicant_detail.html"
    context_object_name = "applican"
    pk_url_kwarg = "id"

class AcceptApplicantDetailView(DetailView):
    model = Applications
    template_name = "emp-acceptcandprofile.html"
    context_object_name = "candaccept"
    pk_url_kwarg = "id"

@signin_required
def reject_application(request,*args,**kwargs):
    app_id=kwargs.get('id')
    qs=Applications.objects.get(id=app_id)
    qs.status='rejected'
    qs.save()
    return redirect('emp-home')

@signin_required
def accept_application(request,*args,**kwargs):
    app_id=kwargs.get('id')
    qs=Applications.objects.get(id=app_id)
    qs.status="accepted"
    qs.save()
    send_mail(
        'Job Notification',
        'Your application is accepted',
        'microsearch143@gmail.com',
        ['rbapvtltd24@gmail.com'],
        fail_silently=True,
    )
    return redirect('emp-listjob')

class AcceptApplicationView(ListView):
    model = Applications
    template_name = "emp-acceptapplist.html"
    context_object_name = "acceptapp"

    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get("id"),status="accepted")