from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import UserRequests
from django.contrib import messages
import sys
import os
import subprocess
import pandas as pd
import csv
import datetime

values_df=pd.DataFrame()

def index(request):
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                #error message put below
                abc= 'User Already exists!'
                return render(request ,'pages/index.html' , {'error': abc})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                #give landing page
                msg="please login now"
                return redirect('about')
        else:
            return render(request ,'pages/landing.html')
    else:
        return render(request,'pages/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('landing')
        else:
            msg = "Username or password is incorrect!"
            return render(request ,'pages/index.html' , {'error': msg})
    else:
        return render(request ,'pages/index.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

def external(request):
    from subprocess import run, PIPE
    OHRID=request.user.username
    #print(u)
    abc=request.POST['url']
    ert=request.POST['subnet']
    ert += "/"
    ert +=request.POST['cidr']
    # dt=request.POST['date']
    # print("this is before" , dt)
    # print(type(dt))
    dt=datetime.datetime.strptime(request.POST['date'],'%Y-%m-%d')
    starttime=datetime.datetime.strptime(request.POST['starttime'],'%H:%M').time()
    endtime=datetime.datetime.strptime(request.POST['endtime'],'%H:%M').time()
    freq=int(request.POST['frequency'])
    z=dt.date()
    # print(abc)
    print(type(ert)) 
    print(ert)
    # print(OHRID)
    query_set = UserRequests.objects.filter(OHRID=int(OHRID), url=abc,subnet=ert, date=z, starttime=starttime, endtime=endtime, frequency=freq, completed=True)
    # query_set = UserRequests.objects.filter(subnet=ert)
    print(query_set)
    if query_set:
        print('exists')
        # messages.success(request,('request already exists for the data'))
    else:
        print('insert')
        writevalues(OHRID,abc,ert,z,starttime,endtime,freq,completed=False)
    # , subnet=request.POST['subnet'])
    # query_set2=UserRequests.objects.filter(OHRID=int(OHRID))
    # print(query_set2)
    # for records in query_set2:
    #     print("below db date types")
    #     print(records.subnet)
    #     print(type(records.subnet))

    url1=str(abc)
    dt1=str(dt)
    st1=str(starttime)
    et1=str(endtime)
    f1=str(freq)     
    values={}
    values['OHRID']=OHRID
    values['url']=abc
    values['subnet']=ert
    values['date']=dt
    values['starttime']=starttime
    values['endtime']=endtime
    values['frequency']=freq

    all_values(values)
    #data=run([sys.executable,'C://Users//Desktop//tt.py',abc , ert],shell=False,stdout=PIPE)
    #print(type(data))
    p = subprocess.Popen(["powershell.exe", 
              "C:\\Users\\Desktop\\aRGpass.ps1",url1,dt1,st1,dt1,et1,f1],
              shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
              #stdout=sys.stdout)
    print(subprocess.STDOUT)
    
    print(subprocess.PIPE)
    out,er = p.communicate()
    print("giving output")
    print(out)
    #print(er)
    out=out.decode("utf-8")
    out=out.strip()
    print(type(out))
    return render(request,'pages/about.html',{'data':out})



def about(request):
    return render(request,'pages/about.html')

def landing(request):
    return render(request,'pages/landing.html')

def all_values(values):
    # print(values)
    # print(values_df)
    filename="C:\\Users\\Desktop\\details.csv"
    with open(filename, 'a') as f:
        writer=csv.writer(f)
        writer.writerow([values['OHRID'], values['url'], values['subnet'],values['date'],values['starttime'],values['endtime'],values['frequency']])


def writevalues(OHRID,abc,ert,z,starttime,endtime,freq,completed=False):
    print(OHRID,abc,ert,z,starttime,endtime,freq,completed)
    # requests=[{"ohrid":OHRID,"url":abc,"subnet":ert,"date":z,"starttime":starttime,"endtime":endtime,"frequency":freq,"completed":"False"}]
    # result=UserRequests.write(requests)
    userdata=UserRequests()
    userdata.OHRID=OHRID
    userdata.url=abc
    userdata.subnet=ert
    userdata.date=z
    userdata.starttime=starttime
    userdata.endtime=endtime
    userdata.frequency=freq
    userdata.completed=False
    userdata.save()

def view_all(request):
    OHRID=request.user.username
    print(OHRID)
    #for i in UserRequests.find():
        #print(i)
    items=UserRequests.objects()
    print(items)
    #items=UserRequests.objects.filter(OHRID=int(OHRID))
    print("in view")
    print(type(items))
    print(items)
    return render(request,'pages/view_all.html',{'data':items})


def delete(request,UserRequests_id):
    item=UserRequests.objects.get(pk=UserRequests_id)
    item.delete()
    messages.success(request,('request data has been deleted!'))
    return redirect('view_all')