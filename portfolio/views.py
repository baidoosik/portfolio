from django.shortcuts import render


# Create your views here.
def main_view(request):
    return render(request,'portfolio/home.html')

def elec_view(request):
    return render(request,'portfolio/home.html')

def startup_view(request):
    return render(request,'portfolio/home.html')

def project_view(request):
    return render(request,'portfolio/home.html')

def experience_view(request):
    return render(request,'portfolio/home.html')

def resume_view(request):
    return render(request,'portfolio/home.html')

def profile_view(request):
    return render(request, 'portfolio/profile.html')
