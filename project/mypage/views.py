from django.shortcuts import render
from django.contrib.auth.decorators import login_required   # 아이디와 이메일 마이페이지에 가져오기 위해 사용했음

def mypage_view(request):
    # 사용자 정보를 세션에서 가져와서 전달함
    username = request.user.username
    email = request.user.email

    return render(request, 'mypage/mypage.html', {'username':username, 'email':email, })

def mypost_view(requset):   # 회원가입을 했을때 로그인한 그 유저가 쓴 글만 불러오도록..

    return render(
        requset,
        'mypage/my-post.html',
    )

def comment_view(requset):   # 회원가입을 했을때 로그인한 그 유저가 쓴 글만 불러오도록..

    return render(
        requset,
        'mypage/comment.html',
    )
