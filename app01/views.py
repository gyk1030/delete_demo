# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib import auth

class Test(APIView):
    def get(self, request, pk):
        print pk
        service_id = request.GET.get('service_id')
        return HttpResponse(service_id)

    def post(self, request):
        # user = request.data.get('name')
        # pwd = request.data.get('pwd')
        print request.session.__dict__
        # if user and pwd:
        #     print user + '+' + pwd
        return JsonResponse(str(request.session.__dict__))

    def delete(self, request, pk):
        print pk
        service_id = request.GET.get('service_id')
        return HttpResponse(service_id)
