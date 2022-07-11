import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def create_category(requests):

    if requests.method == "POST":

        # 디코드를 반드시
        body = json.loads(requests.body.decode('utf-8'))

        new_category = Category.objects.create(
            title = body['title'],
            view_auth = body['view_auth'],
            color = body['color']
        )
    # json 형태로 예쁘게 만들기
        new_category_json = {
            'id' : new_category.id,
            'title' : new_category.title,
            'view_auth' : new_category.view_auth,
            'color' : new_category.color,
        }
        return JsonResponse({
            'status': 200,  #성공
            'success' : True,
            'message': '생성 성공',
            'data': new_category_json

        })

    else:
        return JsonResponse({
            'status': 405,  #실패
            'success' : False,
            'message': '생성 실패',
            'data': None
        })
