from django.urls import path
from employer import views


urlpatterns=[
    path("emphome",views.EmployerHomeView.as_view(),name="e-home"),
    path("profiles/add", views.EmployerProfileCreateView.as_view(), name="emp-profile"),
    path("profiles/details", views.EmployerProfileDetailView.as_view(), name="emp-detail"),
    path("jobs/add",views.JobCreateView.as_view(),name="emp-addjob"),
    path("jobs/all",views.EmployerJobListView.as_view(),name="emp-listjob"),
    path("jobs/detail/<int:id>",views.JobDetailView.as_view(),name="emp-jobdetail"),
    path("view_applic/<int:id>",views.ViewApplication.as_view(),name="view_applic")

]
