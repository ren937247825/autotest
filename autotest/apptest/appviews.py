from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apptest.models import AppCase,AppCaseStep

# Create your views here.


#app用例管理
@login_required
def appcase_manage(request):
    appcase_list = AppCase.objects.all()
    username = request.session.get('user','')   #读取浏览器登录session
    return render(request,'appcase_manage.html',{"user":username,"appcases":appcase_list})


#App用例测试步骤
@login_required
def appcasestep_manage(request):
    username = request.session.get('user','')
    appcasestep_list = AppCaseStep.objects.all()
    return render(request,'appcasestep_manage.html',{"user":username,"appcasesteps":appcasestep_list})