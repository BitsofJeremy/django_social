from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm

# manual setup of login
# def user_login(request):
# 	if request.method == 'POST':
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			cleaned_data = form.cleaned_data
# 			user = authenticate(
# 				request,
# 				username=cleaned_data['username'],
# 				password=cleaned_data['password']
# 			)
# 			if user is not None:
# 				if user.is_active:
# 					login(request, user)
# 					return HttpResponse('Authenticated Successfully')
# 				else:
# 					return HttpResponse('Your Account is Disabled')
# 			else:
# 				return HttpResponse('Invalid Login')
# 	else:
# 		form = LoginForm()
# 	return render(
# 		request,
# 		'account/login.html',
# 		{'form': form}
# 	)


@login_required
def dashboard(request):
	"""
	Render the dashboard and set the section var to dashboard
	"""
	return render(
		request,
		'account/dashboard.html',
		{'section': 'dashboard'}
	)
