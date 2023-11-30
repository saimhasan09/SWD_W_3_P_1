from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    ctx = {'author': 'saim', 'age': 24, 'list':['python', 'is', 'best'], 'birthday':datetime.datetime.now(), 'value' : 10 , 'courses' : [
        {
            'id': 1,
            'name': 'pythons',
            'fees': 2500
        },
        {
            'id': 2,
            'name': 'cpp',
            'fees': 5500
        },
        {
            'id': 3,
            'name': 'Database',
            'fees': 3500
        },
        
    ], 'months': "January - February - March", 
    'users': [
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
]}
    return render(request,'first_app/index.html', ctx)


def about(request):
    return render(request,'first_app/about.html')

def contact(request):
    return render(request,'first_app/contact.html')
