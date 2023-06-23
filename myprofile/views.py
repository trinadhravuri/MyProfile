from django.shortcuts import render,redirect
from .models import Enquiry
from .forms import EnquiryForm
from django.http import HttpResponseRedirect
# Create your views here.
all_skills = [
    {
        'skillname':'Python',
        'skillid':0,
        'skillimage':'py.png',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
        {
        'skillname':'Automation Testing',
        'skillid':1,
        'skillimage':'auto1.jpg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
    {
        'skillname':'Django',
        'skillid':2,
        'skillimage':'django1.png',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
        {
        'skillname':'Full Stack Dev',
        'skillid':3,
        'skillimage':'fs2.jpg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
      {
        'skillname':'REST API',
        'skillid':4,
        'skillimage':'ns.jpg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
    {
        'skillname':'pandas',
        'skillid':5,
        'skillimage':'pandas1.png',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
    {
        'skillname':'flask',
        'skillid':6,
        'skillimage':'flask1.png',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
    {
        'skillname':'Network Security',
        'skillid':7,
        'skillimage':'ns.jpg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
      {
        'skillname':'HTML',
        'skillid':8,
        'skillimage':'ns.jpg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
      {
        'skillname':'C S S',
        'skillid':9,
        'skillimage':'ns.jpg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
      {
        'skillname':'JavaScript',
        'skillid':10,
        'skillimage':'ns.jpg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
]
all_projects = [
     {
        'projectname':'InFlight Entertainment System',
        'projectid':1,
        'projectimage':'inflight.png',
        'projectsummary':'',
        'Teamsize':5,
        'period':'05-2021 to 11-2021',
        'Roles':'''
        
        ''',
    },
    {
        'projectname':'Global Manufacturing Execution System',
        'projectid':2,
        'projectimage':'global.jpeg',
        'projectsummary':'This project is mainly intended to Developand maintaining Automation Tests for Web application using the Python selenium in timely, cost effectively manner.',
        'Teamsize':5,
        'period':'07-2019 to 05-2021',
        'Roles':'''
        
        ''',
    },
    {
        'projectname':'Dose WatchApplication',
        'projectid':3,
        'projectimage':'dose.jpg',
        'projectsummary':'This project is intended to develop the Automation test cases using the Python and Selenium with  PyCharm IDE.',
        'Teamsize':4,
        'period':'01-2018 to 07-2019',
        'Roles':'''
        
        ''',
    },
    {
        'projectname':'DCAR ELO',
        'projectid':4,
        'projectimage':'dcarecg1.jpeg',
        'projectsummary':'MACVU360 is an ECG Machine which is developed on an Embedded Linux platform',
        'Teamsize':3,
        'period':'01-2017 to 12-2017',
        'Roles':'''
        
        ''',
    },
    {
        'projectname':'Course Attendance Tracking Application : manual testing',
        'projectid':5,
        'projectimage':'courseattendance.jpeg',
        'projectsummary':'Course Attendance Tracking Application is an INSTITUTIOAL application that tracks the attendance of the students.',
        'Teamsize':4,
        'period':'04-2016 to 12-2016',
        'Roles':'''
        
        ''',
    },
    {
        'projectname':'VAS Application : manual testing',
        'projectid':6,
        'projectimage':'vas.jpeg',
        'projectsummary':'VAS application is VALUE ADDED SERVICES application for the basic mobiles that uses the services..',
        'Teamsize':4,
        'period':'09-2015 to 03-2016',
        'Roles':'''
        
        ''',
    },
    
]
def home(request):
    form = EnquiryForm
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    context ={
        'skills':all_skills[:4],
        'projects':all_projects[:3],
        'form':form
        }
    return render(request,'myprofile/home.html',context)

def base(request):
    return render(request,'myprofile/base.html')

def allskills(request):
    context ={
        'skills':all_skills,
    }
    return render(request,'myprofile/allskills.html',context)

def allprojects(request):
    context = {
        'projects':all_projects,
    }
    return render(request,'myprofile/allprojects.html',context)

def enquiryform(request):
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = {
        'form':form
    }
    return render(request,'myprofile/includes/enquiry.html',context)