from django.shortcuts import get_object_or_404
from .models import *
from django.http.response import JsonResponse
import json

# Create your views here.
def create_category(request):
    # 생성 과정은 post 요청에만 일어나도록!
    if request.method == "POST":

        # requests에 담겨서 온 데이터를 디코딩하기!(사용할 수 있도록 json 화)
        body =  json.loads(request.body.decode('utf-8'))
        
        # new_category변수에는 orm을 통해 생성된 결과가 들어가요!
        # 장고 orm 을 통해 가져온 데이터의 자료형은 "queryset"이라는 특별한 자료형입니다.
        new_category = Category.objects.create(
            # requests에서 넘어온 데이터로 새로운 Category 생성)
            title       =  body['title'],
            view_auth   =  body['view_auth'],
            color       =  body['color']
        )

        # queryset 자료를 json 모양으로 데이터를 이쁘게 정리해주기
        new_category_json={
            "id"        : new_category.id,
            "title"     : new_category.title,
            "view_auth" : new_category.view_auth,
            "color"     : new_category.color,
            "pup_date"  : new_category.pup_date,
        }

        # 성공 할 경우 client가 받을 데이터 모양
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '생성 성공!',
                'data': new_category_json    # 이쁘게 만든 데이터를 respons['data']에 담아 보내줌
            })

    # request.method에 대한 분기처리(post 가 아닌경우)
    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
        })

def get_category_all(requests):
    if requests.method == 'GET':
        category_all = Category.objects.all() # 쿼리셋 모양

        ###
        Category.objects.filter(view_auth = 0) # 여러개
        get_object_or_404(Category, pk = 2) # 하나만 
        Category.objects.get(pk = 2) # 하나만
        ###

        # 이쁘게 만들기
        category_json_all=[]
        for category in category_all:
            category_json={
                "id"        : category.id,
                "title"     : category.title,
                "view_auth" : category.view_auth,
                "color"     : category.color,
                "pup_date"  : category.pup_date,
            }
            category_json_all.append(category_json) # 나중에 serializer 배우면 생략 가능한 부분!!
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'category_all 수신 성공!',
                'data': category_json_all
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

def get_category(request, id):
    if request.method == "GET":
        category = get_object_or_404(Category,pk = id)
        category_json={
                "id"        : category.id,
                "title"     : category.title,
                "view_auth" : category.view_auth,
                "color"     : category.color,
                "pup_date"  : category.pup_date,
        }
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'category 수신 성공!',
                'data': category_json
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

def update_category(request, id):
    if request.method == "PATCH":
        body =  json.loads(request.body.decode('utf-8'))
        update_category = get_object_or_404(Category, pk = id)
        update_category.title = body['title']
        update_category.view_auth = body['view_auth']
        update_category.color = body['color']
        update_category.save()
        
        # 이쁘게 만들기
        update_category_json={
            "id"        : update_category.id,
            "title"     : update_category.title,
            "view_auth" : update_category.view_auth,
            "color"     : update_category.color,
            "pup_date"  : update_category.pup_date,
        }

        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '업데이트 성공!',
                'data': update_category_json
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

def delete_category(request, id):
    if request.method == "DELETE":
        delete_category = get_object_or_404(Category, pk = id)
        delete_category.delete()
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '삭제 성공!',
                'data': None
            })
    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })


def create_todo(request, category_id):
    if request.method == "POST":
        
        body = request.POST
        img = request.FILES['thumb_nail']

        new_todo = Todo.objects.create(
            category = get_object_or_404(Category, pk = category_id),
            content = body["content"],
            thumb_nail = img
        )
   
        new_todo_json={
            "id" : new_todo.id,
            "content" : new_todo.content,
            "thumb_nail" : "/media/"+ str(new_todo.thumb_nail),
            "is_completed" : new_todo.is_completed,
            "pup_date" : new_todo.pup_date
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


def get_todo_all(request, category_id):
    if request.method == "GET":
        category_todo = Todo.objects.filter(category = category_id)
        
        category_todo_json=[]
        for todo in category_todo:
            new_set={
                "todo_id" : todo.id,
                "content" : todo.content,
                "thumb_nail" : "/media/" + str(todo.thumb_nail),
                "is_completed" : todo.is_completed,
                "pup_date" : todo.pup_date
            }
            category_todo_json.append(new_set)
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo_all 수신 성공!',
                'data': category_todo_json
            })

    return JsonResponse({
            'status': 405,
            'success': False,
            'message': 'method error',
            'data': None
        })

def get_todo(request, todo_id):
    if request.method == "GET":
        todo = get_object_or_404(Todo,pk = todo_id)
        todo_json={
                "todo_id" : todo.id,
                "content" : todo.content,
                "thumb_nail" : "/media/" + str(todo.thumb_nail),
                "is_completed" : todo.is_completed,
                "pup_date" : todo.pup_date
        }
        
        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo 수신 성공!',
                'data': todo_json
            })

    return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })

def update_todo(request, todo_id):
    if request.method == "POST":
        
        body = request.POST
        img = request.FILES['thumb_nail']

        update_todo = get_object_or_404(Todo,pk = todo_id)
        update_todo.content = body['content']
        update_todo.is_completed = body['is_completed']
        update_todo.thumb_nail = img
        update_todo.save()

        
        update_todo_json={
            "id" : update_todo.id,
            "content" : update_todo.content,
            "thumb_nail" : "/media/"+ str(update_todo.thumb_nail),
            "is_completed" : update_todo.is_completed,
            "pup_date" : update_todo.pup_date
        }

        return JsonResponse({
            'status': 200,
            'success': True,
            'message': 'Todo 업데이트 성공!',
            'data': update_todo_json
        })

    return JsonResponse({
        'status': 405,
        'success': False,
        'message': 'method error',
        'data': None
    })

def delete_todo(request, todo_id):
    if request.method == "DELETE":
        delete_todo = get_object_or_404(Todo, pk = todo_id)
        delete_todo.delete()

        return JsonResponse({
                'status': 200,
                'success': True,
                'message': 'todo 삭제 성공!',
                'data': None
            })

    return JsonResponse({
            'status': 405,
            'success': False,
            'message': 'method error',
            'data': None
        })