# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse

# Create your views here.
from rest_framework.views import APIView

class Test(APIView):
    def get(self,request, pk):
        print pk
        service_id = request.GET.get('service_id')
        return HttpResponse(service_id)

    def delete(self, request ,pk):
        print pk
        service_id = request.GET.get('service_id')
        return HttpResponse(service_id)