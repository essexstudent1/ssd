from django.shortcuts import render

# Create your views here.

# Define the GROUP1 home page view
def home_view(request):
    user = request.user
    return render (request, 'report/home.html')
 
