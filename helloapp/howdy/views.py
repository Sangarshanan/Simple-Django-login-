from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


#disabling csrf (cross site request forgery)
@csrf_exempt
def index(request):
    #if post request came 
    if request.method == 'POST':
        #getting values from post
        name = request.POST.get('name')
        passwd = request.POST.get('passwd')


        #adding the values in a context variable 
        context = {
            'name': name,
            'passwd': passwd
        }
        user = authenticate(username=name, password=passwd)
        if user is not None:
            template = loader.get_template('showdata.html')
        else:
            return HttpResponse("<h1> WRONG CREDENTIALS </h1>")
        #returing the template 
        return HttpResponse(template.render(context, request))
    else:
        #if post request is not true 
        #returing the form template 
        template = loader.get_template('index.html')
        return HttpResponse(template.render())