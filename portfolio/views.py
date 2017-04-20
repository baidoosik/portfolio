import os
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse,JsonResponse



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

def resume_view(request):# 이력서 다운로드.
    # 엑셀 다운로드 응답하기
    filepath = '/Users/doosikbai/worldnomade/portfolio/static/portfolio/assets/resume.pages'
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.pages')
        # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response

    return render(request,'portfolio/home.html')

def profile_view(request):
    return render(request, 'portfolio/profile.html')
