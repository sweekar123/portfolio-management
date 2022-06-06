from django.urls import path
from resume.views import ResumeListView,ResumeCreateView,ResumeDetailView
urlpatterns = [
	path("",ResumeListView.as_view(),name="resume-list"),
	path("create/",ResumeCreateView.as_view(),name="resume-create"),
	path("resume/<id>",ResumeDetailView.as_view(),name="resume-detail")
]