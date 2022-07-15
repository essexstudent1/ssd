from django.shortcuts import render, redirect

# the following imports are required for SSD
from django.contrib.auth import login, authenticate, logout
from report.forms import (
  UserRegistrationForm, 
  UserAuthenticationForm,
  UserMFAAuthenticationForm,
)

# Define the GROUP1 SSD home page view
def home_view(request):
    user = request.user
    if user.is_authenticated: 
        if user.is_mfa_authenticated == False:
          logout(request)
    return render (request, 'report/home.html')


# Define the SSD new user registration view
# this code is adapted from https://www.youtube.com/watch?v=oZUb372g6Do&list

def registration_view(request):
  context={}
  user = request.user

  # If the user is already authenticated, they don't need to register an 
  # account, so the application redirects them to the home page.
  if user.is_authenticated: 
    return redirect("home")

  # This section of code processes completed (POSTed) forms
  if request.method == "POST":
    form = UserRegistrationForm(request.POST)

    # if the completed form is valid, save the user and 
    # consider them authenticated  
    if form.is_valid():
      form.save()
      email = form.cleaned_data.get('email')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(email=email, password=raw_password)
      login(request, user)
      user.is_mfa_authenticated = True
      user.save()
      return redirect('home')
    
    else:
      context['register_form'] = form
  
  else:
    form = UserRegistrationForm()
    context['register_form'] = form

  return render (request, 'report/register.html', context)


# Define the SSD logout view
# This view simply logs the user out and redirects to the home page

def logout_view(request):
    logout(request)
    return redirect('home')


# Define the SSD user login view
# this code is adapted from https://www.youtube.com/watch?v=tTvSl3RHBjE

def login_view(request):
  context={}
  user = request.user

  # If the user is already authenticated, redirect to home
  if user.is_authenticated: 
    return redirect("home")

  # This section of code processes completed (POSTed) forms
  if request.method == "POST":
    form = UserAuthenticationForm(request.POST)
    
    # If the form is valid, authenticate the user 
    if form.is_valid():
      email = form.cleaned_data.get('email')
      password = form.cleaned_data.get('password')
      user = authenticate(email=email, password=password)

      # Log in the user and then redirect them to the MFA validation page
      if user:
        login(request, user)
        user.is_mfa_authenticated = False
        user.mfa_attempts = 0
        user.save()
        return redirect('mfa_login')
    
  else:
    form = UserAuthenticationForm()
  
  context['login_form'] = form
  return render (request, 'report/login.html', context)


# Define the SSD user 2FA validation view

def mfa_login_view(request):
  context={}
  user = request.user

  # This sets the 2FA validation attempt limit to 5 tries. Ideally, this 
  # would be a configuration setting rather than hardcoded.
  mfa_limit = 5

  # If the user is not authenticated yet, redirect them to the login view
  if not user.is_authenticated:
    return redirect('login')

  # If the user has already passed 2FA validation, redirect to home view
  if user.is_mfa_authenticated: 
    return redirect('home')

  # This section of code processes completed (POSTed) forms
  if request.method == "POST":
    form = UserMFAAuthenticationForm(request.POST)

    # If the form is valid, attempt to validate the user  
    if form.is_valid():
      security_answer = form.cleaned_data.get('security_answer')
      
      # check if the security answer is correct. If so,
      # 2FA authenticated to TRUE and redirect to home view
      if user.security_answer == security_answer:
        user.is_mfa_authenticated = True
        user.save()
        return redirect('home')

      # If security answer is not correct, increment 2FA attempt counter.
      # If counter exceeds attempt limit, log the user out.
      else:
        user.mfa_attempts = user.mfa_attempts + 1
        user.save()
        if user.mfa_attempts > mfa_limit:
          logout(request)
          return redirect('home')

        context['attempts'] = "2FA validation failed. You may try " + str(mfa_limit - user.mfa_attempts) + " more times"
    
  else:
    form = UserMFAAuthenticationForm()
    
  context['mfa_login_form'] = form
  context['security_question'] = user.security_question
  return render (request, 'report/mfa_login.html', context)


# Report breach page

def  breach_report_view(request):
  context={}
  form = ReportForm()
  if request.method == "POST":
    form = ReportForm(request.POST)
    if form.is_valid():
      form.save()
  
  context['report_form'] = form
  form = ReportForm()
  return render (request, 'report/reportdatabreach.html', context)
  
  

