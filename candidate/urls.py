from django.urls import path
from candidate import views

urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name="cand-home"),
    path("profiles/add",views.CandidateProfileCreateView.as_view(),name="cand-addprofile"),
    path("profiles/details",views.CandidateProfileDetailView.as_view(),name="cand-detailprofile"),
    path("profiles/change<int:id>",views.CandidateProfileEditView.as_view(),name="cand-editprofile"),
    path("jobs/details/<int:id>",views.CandidateJobDetailView.as_view(),name="cand-detailjob"),
    path("application/add/<int:id>",views.apply_now,name="apply_now"),
    path("profiles/applied",views.MyApplicationView.as_view(),name="cand-appliedjobs"),
    path("app/accepted",views.AcceptedApplicationsView.as_view(),name="cand-acceptjob")
]