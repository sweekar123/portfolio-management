from django.shortcuts import render,redirect ,get_object_or_404
from .models import Resume
from .forms import ResumeForm
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView

# Create your views here.

class ResumeListView(ListView):
	template_name = "resume/resume_list.html"
	queryset = Resume.objects.all()

class ResumeCreateView(CreateView):
	template_name="resume/resume_create.html"
	form_class = ResumeForm
	queryset = Resume.objects.all()

class ResumeDetailView(DetailView):
	template_name = "resume/resume_detail.html"
	queryset = Resume.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Resume,id=id_)