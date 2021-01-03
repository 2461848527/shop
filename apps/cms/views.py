from django.shortcuts import render

# Create your views here.
def index(request):
    '''首页'''
    return render(request,'cms/cms.html')

def allfind(request):
    '''首页'''
    return render(request,'cms/allFiind.html')

def book(request):
    return render(request,'cms/book01.html')

def evaluate(request):
    return render(request,'cms/evaluate.html')

def handlestatic(request):
    return render(request,'cms/handleStatic.html')

def meetfind(request):
    return render(request,'cms/meetfind.html')

def mymes(request):
    return render(request,'cms/myMes.html')

def notice(request):
    return render(request,'cms/notice.html')

def sumtable(request):
    return render(request,'cms/sumTable.html')
