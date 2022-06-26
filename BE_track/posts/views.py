from http.client import HTTPResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def http_response(request):
    if request.method =="GET":
        return HTTPResponse("hello world")

def json_response(request):
    if request.method =="GET":
        data={
            'name':'hw',
            'school':'cau'
        }
        
        return JsonResponse(data=data)


# Create your views here.
@csrf_exempt
def index(request):
    if request.method=='POST':
        name=request.POST.get('name')
        data={
            'name' : name
        }
        return render(request,'index.html',context=data)
    else:
        return render(request,'index.html')
