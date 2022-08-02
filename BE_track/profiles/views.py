from unicodedata import name
from django.shortcuts import get_object_or_404
from .models import *
from django.http.response import JsonResponse
import json

# Create your views here.
def create_profile(request):
    # 생성 과정은 post 요청에만 일어나도록!
    if request.method == "POST":

        # requests에 담겨서 온 데이터를 디코딩하기!(사용할 수 있도록 json 화)
        body =  json.loads(request.body.decode('utf-8'))
        
        # 장고 orm 을 통해 가져온 데이터의 자료형은 "queryset"이라는 특별한 자료형입니다.
        new_profile = Profile.objects.create(
            # requests에서 넘어온 데이터로 새로운 Category 생성)
            name       =  body['name'],
            age   =  body['age'],
            phone       =  body['phone']
        )

        # queryset 자료를 json 모양으로 데이터를 이쁘게 정리해주기
        new_profile_json={
            "name"        : new_profile.name,
            "age"     : new_profile.age,
            "phone" : new_profile.phone,
        }

        # 성공 할 경우 client가 받을 데이터 모양
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '생성 성공!',
                'data': new_profile_json    # 이쁘게 만든 데이터를 respons['data']에 담아 보내줌
            })

    # request.method에 대한 분기처리(post 가 아닌경우)
    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
        })

## category 로 생성된 모든 데이터를 가져오는 함수
def get_profile_all(requests):
    # 생성 과정은 get 요청에만 일어나도록!
    if requests.method == 'GET':
        # 쿼리셋 모양으로 가져옴(쿼리셋 모양은 for문 적용 가능)
        profile_all = Profile.objects.all() 

        ### 특정 속성의 category 여러개를 가져오고 싶을 때 ### 
        #Profile.objects.filter(view_auth = 0) # 여러개
        ###

        profile_json_all=[] 
        for profile in profile_all:
            category_json={
                "name"        : profile.name,
                "age"     : profile.age,
                "phone" : profile.phone,
            }
            profile_json_all.append(category_json) 
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'category_all 수신 성공!',
                'data': profile_json_all
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })


def create_content(request, profile_id):
    if request.method == "POST":
        
        
        new_content = Content.objects.create(
            profile = get_object_or_404(Profile, pk = profile_id),
            content = request.POST.get('content','')
        )
   
        new_todo_json={
            "id" : new_content.id,
            "content" : new_content.content,
        }
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo 생성 성공!',
                'data': new_todo_json
            })


    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
        })

def get_content_all(request, profile_id):
    if request.method == "GET":
        profile_content = Content.objects.filter(profile = profile_id)
        
        profile_content_json=[]
        for content in profile_content:
            new_set={
                "content_id" : content.id,
                "content" : content.content,
            }
            profile_content_json.append(new_set)
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo_all 수신 성공!',
                'data': profile_content_json
            })

    return JsonResponse({
            'status': 405,
            'success': False,
            'message': 'method error',
            'data': None
        })

