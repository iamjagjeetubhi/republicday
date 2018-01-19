# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponseRedirect, HttpResponse
import re
from urllib.request import urlretrieve
from urllib.parse import quote

# Create your views here.
def index(request):
    return render(request, 'index_1.html')
def myprofileview(request, username):
    name = username.replace("_", " ")
    domain = request.get_host()
    path = request.get_full_path()
    url = domain+path
    message = "Hi, i'm *%s*\n"%(username)+"Wishing you *HAPPY REPUBLIC DAY* in advance 👇\n"
    message = quote(message)
    message = message+url
    print(message)
    return render(request, 'user_1.html',{
        'name': name,
        'message':message,
        })


@csrf_exempt
def userlink(request):
    #try:
    if request.method == 'POST':
        data = request.POST
        import pdb
        name = data['name']
        name_original = re.sub(r'\b[a-z]', lambda m: m.group().upper(), name)
        name_link= name.replace(" ", "_")
        print(name)
        domain = request.get_host()
        path = name_link
        url = domain+"/"+path
        message = "Hi, i'm *%s*\n"%(name_original)+"Wishing you *HAPPY REPUBLIC DAY* in advance 👇\n"
        message = quote(message)
        message = message+url
        print(message)
        return render(request, 'profile_1.html',{
            'name': name,
            'message':message,
            })


            
   # except:
    #    print("end exception")
     #   return HttpResponse(json.dumps({'mesg': "failed"}), content_type='application/json')
