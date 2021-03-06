from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect, HttpResponse

class UserRegisterView(FormView):
	template_name = 'registration/signup.html'
	form_class = UserRegisterForm
	success_url = '/'

	def form_valid(self,form):
		username = form.cleaned_data.get('username')
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get("password")
		new_user = User.objects.create(username=username,email=email)
		new_user.set_password(password)
		new_user.save()
		## creeate users
		user = authenticate(username=username, password=password)
		if user is not None:
			login(self.request, user)
			messages.success(self.request, "Hi there, thanks for register!")
		else:
			messages.warning(self.request, "invalid stuff")
		## log user in
		return super(UserRegisterView, self).form_valid(form)


def my_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
			message = messages.success(request, "You are logged in. Hi!!")
			return HttpResponseRedirect("/")
		else:
			message = messages.success(request, "Nope, wrong user name or password")
			return HttpResponseRedirect("/login/")
	return auth_views.login(request,"registration/login.html/")

@login_required
def my_logout(request):
	messages.success(request, "See you!")
	return auth_views.logout(request,"/")


def home(request):

	queryset = Post.objects.order_by("-created")[:3]
	object_list = {
	'object_list':queryset
	}
	# messages.success(request, 'Hello world!')
	return render(request,"to_be_frank/home.html",object_list)


def contact(request):
	return render(request,"to_be_frank/contact.html",{})

def about(request):
	return render(request,"to_be_frank/about.html",{})


def post(request):
	return render(request,"to_be_frank/post.html",{})
