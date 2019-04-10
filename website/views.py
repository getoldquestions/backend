from django.shortcuts import render, redirect
from .models import Contact, Questions
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView


def index(request):
	
	contact_form = ContactForm(request.POST or None)
	context = {'form': contact_form}
	
	return render(request, "website/index.html", context)

def contact(request):
	contact_form = ContactForm(request.POST or None)
	context={
		'form': contact_form  
	}
	if request.method == 'POST':
		
		if contact_form.is_valid():
			r_name = request.POST.get('name')
			r_email = request.POST.get('email')
			r_message = request.POST.get('message')
			c= Contact(name = r_name, email = r_email, message = r_message)
			c.save()

			messages.success(request, f'Your messsage is sent. Thank you for your suggestion.')
			return render(request, 'website/index.html', {'form': ContactForm()})

	else:
		form = ContactForm()
	messages.warning(request, f"Your messsage was not sent. Please check 'Contact Us' section for error.")
	return render(request, 'website/index.html',context )

	#if request.method == 'POST':
	#	r_name = request.POST.get('name')
	#	r_email = request.POST.get('email')
	#	r_message = request.POST.get('message')
	#	messages.success(request, f'Your messsage is sent. Thank you for your suggestion.')

	#	c= Contact(name = r_name, email = r_email, message = r_message)
	#	c.save()

	#	return render(request, "website/index.html")
	#else:
	#	return render(request, "website/index.html")

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
	fields = ['name', 'level', 'year', 'faculty', 'semester',  'file','date_posted']
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

def plus2(request):
	return render(request, 'website/+2.html')

class questionsView(ListView):
	model = Questions
	template_name = 'website/files+2.html'
	context_object_name= 'files'
	ordering = ['-date_posted']

	
class semesterView(ListView):
	model = Questions
	template_name = 'website/sems.html'

def semdetailView(request):
	return render(request, 'website/sems')






