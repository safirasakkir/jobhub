from django.urls import path
from candidate import views

urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name="cand-home"),
    path("profiles/add",views.CandidateProfileCreateView.as_view(),name="cand-addprofile"),
    path("jobs/details/<int:id>",views.CandidateJobDetailView.as_view(),name="cand-detailjob"),
    path("application/add/<int:id>",views.apply_now,name="apply-now"),
    path("myapp",views.MyApplicationView.as_view(),name="my_app"),
]