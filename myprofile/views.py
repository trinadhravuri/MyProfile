from django.shortcuts import render

# Create your views here.
all_skills = [
    {
        'skillname':'Python',
        'skillid':0,
        'skillimage':'py.jpeg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
    {
        'skillname':'Django',
        'skillid':1,
        'skillimage':'django.jpeg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
    {
        'skillname':'pandas',
        'skillid':2,
        'skillimage':'pandas.jpeg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
    {
        'skillname':'flask',
        'skillid':3,
        'skillimage':'flask.png',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
    {
        'skillname':'Automation Testing',
        'skillid':4,
        'skillimage':'testing.jpeg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
    {
        'skillname':'Full Stack Dev',
        'skillid':5,
        'skillimage':'fs.png',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
    {
        'skillname':'Network Security',
        'skillid':6,
        'skillimage':'ns.jpeg',
        'skillcontent':'',
        'skillability':75,
        'skilldescription':'''
        
        ''',
    },
]
all_projects = [
     {
        'projectname':'Freelancing',
        'projectid':0,
        'projectimage':'freelance.png',
        'projectsummary':'Freelancing giving the time to practice more and gain knowledge as well',
        'Teamsize':5,
        'period':'present',
        'Roles':'''
        
        ''',
    },
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
    return render(request,'myprofile/home.html',{'skills':all_skills})

