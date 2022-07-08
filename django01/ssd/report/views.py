from django.shortcuts import render

# Create your views here.

# Define the GROUP1 home page view
def home_view(request):
    return render (request, 'report/home.html')
 
