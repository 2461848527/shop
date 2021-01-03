from django.urls import path,include
from . import views

app_name = 'cms'

urlpatterns = [
    path('',views.index,name='index'),
    path('allfind/',views.allfind,name='allfind'),
    path('book/',views.book,name='book'),
    path('evaluate/',views.evaluate,name='evaluate'),
    path('handlestatic/',views.handlestatic,name='handlestatic'),
    path('meetfind/',views.meetfind,name='meetfind'),
    path('mymes/',views.book,name='mymes'),
    path('notice/',views.book,name='notice'),
    path('sumtable/',views.book,name='sumtable'),
]


