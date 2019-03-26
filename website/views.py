from django.shortcuts import render
from .models import Contact, Questions
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView
def index(request):
	return render(request, "website/index.html")

def contact(request):
	if request.method == 'POST':
		r_name = request.POST.get('name')
		r_email = request.POST.get('email')
		r_message = request.POST.get('message')
		messages.success(request, f'Your messsage is sent. Thank you for your suggestion.')

		c= Contact(name = r_name, email = r_email, message = r_message)
		c.save()

		return render(request, "website/index.html")
	else:
		return render(request, "website/index.html")

class message(LoginRequiredMixin, ListView):
	model = Contact
	template_name = "website/messages.html"
	context_object_name= 'messages'
	ordering = ['-date_posted']
	paginate_by = 5

	login_url = "/admin/login"
	redirect_field_name = "hollaback"
	raise_exception = False
	#redirect_unauthenticated_users = True

class FileCreate(LoginRequiredMixin, CreateView):
	model = Questions
	fields = ['name', 'level', 'semester', 'faculty', 'file','date_posted']
	login_url = "/admin/login"
	redirect_field_name = "hollaback"
	raise_exception = False

class FilesView(ListView):
	model = Questions
	template_name = "website/files.html"
	context_object_name= 'files'
	ordering = ['-date_posted']
	paginate_by = 5

class FilesDetailView(DetailView):
	model = Questions
	template_name = "website/details.html"
	context_object_name= 'file'

class FileDelete(DeleteView):
	model = Questions
	success_url = reverse_lazy("files-view")

		




