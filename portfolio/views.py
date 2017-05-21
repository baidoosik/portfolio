import os
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Post
from .forms import PostForm


# 상단 메뉴
def main_view(request):
    post = Post.objects.all()

    return render(request,'portfolio/home.html',{
        'form':post
    })

def elec_view(request):
    post = Post.objects.filter(category="Electronic-Eng").all()

    return render(request,'portfolio/project_list.html',{
        'form':post
    })

def startup_view(request):
    post = Post.objects.filter(category="Start-up").all()

    return render(request,'portfolio/project_list.html',{
        'form':post
    })

def project_view(request):
    post = Post.objects.filter(category="Project").all()

    return render(request,'portfolio/project_list.html',{
        'form':post
    })

def experience_view(request):
    post = Post.objects.filter(category="Experience").all()

    return render(request,'portfolio/project_list.html',{
        'form':post
    })


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

def post_detail_cowdogting(request):
    post = Post.objects.filter(url="post_detail_cowdogting")

    return render(request, 'portfolio/cowdogting.html',{
        'post':post
    })

def post_detail_toilet(request):
    post = Post.objects.filter(url="post_detail_toilet")
    return render(request, 'portfolio/toilet.html',{
        'post':post
    })

def post_detail_global(request):
    post = Post.objects.filter(url="post_detail_global_challenge")

    return render(request, 'portfolio/global_challenge.html',{
        'post':post
    })
