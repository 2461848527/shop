from django.shortcuts import render


# Create your views here.


def index(request):
    '''首页'''
    content = request.session.get('msg')
    print(content, '&'*100)
    return render(request,'dianzhuang/index.html', {'content': content})

def design(request):
    '''设计页'''
    return render(request,'dianzhuang/design.html')

def youshi(request):
    '''优势页'''
    return render(request,'dianzhuang/youshi.html')

def case(request):
    '''案例页'''
    return render(request,'dianzhuang/case.html')

def team(request):
    '''团队页'''
    return render(request,'dianzhuang/team.html')

def about(request):
    '''关于页'''
    return render(request,'dianzhuang/about.html')

def news(request):
    '''咨询页'''
    return render(request,'dianzhuang/news.html')

def contact(request):
    '''联系页'''
    return render(request,'dianzhuang/contact.html')


