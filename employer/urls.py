from django.urls import path
from employer import views

urlpatterns=[
    path("emphome",views.EmployerHomeView.as_view(),name="emp-home"),
    path("profiles/add",views.EmployerProfileCreateView.as_view(),name="emp-profile"),
    path("profiles/details",views.EmployeeProfileDetailView.as_view(),name="emp-detail"),
    path("profiles/change/<int:id>",views.EmployerProfileEditView.as_view(),name="emp-editpro"),
    path("jobs/add",views.JobCreateView.as_view(),name="emp-addjob"),
    path("jobs/all",views.EmployerJobListView.as_view(),name="emp-listjob"),
    path("jobs/detail/<int:id>",views.JobDetailView.as_view(),name="emp-detailjob"),
    path("jobs/change/<int:id>",views.JobEditView.as_view(),name="emp-editjob"),
    path("jobs/applapps/<int:id>",views.ViewApplicationView.as_view(),name="emp-viewapp"),
    path("jobs/acceptapp/<int:id>",views.AcceptApplicationView.as_view(),name="emp-acceptapplist"),
    path("jobs/candacceptapp<int:id>,",views.AcceptApplicantDetailView.as_view(),name="emp-acceptappdetail"),
    path("jobs/candprofile/<int:id>",views.ApplicantDetailView.as_view(),name="emp-viewprofile"),
    path("status/reject/<int:id>",views.reject_application,name="reject"),
    path("status/accept/<int:id>",views.accept_application,name="accept")

]