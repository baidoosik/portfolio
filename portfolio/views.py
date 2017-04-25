import os
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Post
from .forms import PostForm


# Create your views here.
def main_view(request):
    post = Post.objects.all()

    return render(request,'portfolio/home.html',{
        'form':post
    })

def elec_view(request):
    return render(request,'portfolio/home.html')

def startup_view(request):
    return render(request,'portfolio/home.html')

def project_view(request):
    post = Post.objects.filter(category="Project").all()

    return render(request,'portfolio/project_list.html',{
        'form':post
    })

def experience_view(request):
    return render(request,'portfolio/home.html')


# 이력서 다운로드.
def resume_view(request):
    # 엑셀 다운로드 응답하기
    filepath = '/Users/doosikbai/worldnomade/portfolio/static/portfolio/assets/resume.pages'
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.pages')
        # 필요한 응답헤더 세팅
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response

    return render(request,'portfolio/home.html')

# profile 화면
def profile_view(request):
    return render(request, 'portfolio/profile.html')

# post 작성
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            post = form.save()
            return(Post)
    else:
        form = PostForm()

    return render(request,'portfolio/post_form.html',{
        'form':form
    })


