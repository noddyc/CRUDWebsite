from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from DatabaseApp.models import apis,mashs
from DatabaseApp.serializers import DepartmentSerializer,MashSerializer
from django.db.models import Q



def home(request):
    return render(request, 'index.html')

def updatedQuery(request):
    updatedYear = request.GET['updated']
    departments=apis.objects.filter(updated__startswith=updatedYear)
    departments_serializer = DepartmentSerializer(departments, many=True)
    output = []
    for qrs in departments_serializer.data:
        temp = {}
        temp["id"] = str(qrs['id'])
        temp["apiId"] = qrs['apiId'] 
        temp["updated"]  = qrs['updated'] 
        output.append(temp)
    return render(request, 'updatedQuery.html', {"updated":output})

def protocolsQuery(request):
    protocols = request.GET['protocols']
    departments=apis.objects.filter(protocols=protocols)
    departments_serializer = DepartmentSerializer(departments, many=True)
    output = []
    for qrs in departments_serializer.data:
        temp = {}
        temp["id"] = str(qrs['id'])
        temp["apiId"] = qrs['apiId'] 
        temp["protocols"]  = qrs['protocols'] 
        output.append(temp)
    return render(request, 'protocolsQuery.html', {"protocols":output})

def categoryQuery(request):
    categoryVal = request.GET['category']
    departments=apis.objects.filter(category=categoryVal)
    departments_serializer = DepartmentSerializer(departments, many=True)
    output = []
    for qrs in departments_serializer.data:
        temp = {}
        temp["id"] = str(qrs['id'])
        temp["apiId"] = qrs['apiId'] 
        temp["category"]  = qrs['category'] 
        output.append(temp)
    return render(request, 'categoryQuery.html', {"category":output})

def ratingQuery(request):
    ratingVal = request.GET['rating']
    sign = request.GET['sign']
    if(sign=="gt"):
        departments=apis.objects.filter(rating__gt = ratingVal)
    elif(sign=="lt"):
        departments=apis.objects.filter(rating__lt = ratingVal)
    elif(sign=='eq'):
        departments=apis.objects.filter(rating= ratingVal)
    departments_serializer = DepartmentSerializer(departments, many=True)
    output = []
    for qrs in departments_serializer.data:
        temp = {}
        temp["id"] = str(qrs['id'])
        temp["apiId"] = qrs['apiId'] 
        temp["rating"]  = qrs['rating'] 
        output.append(temp)
    return render(request, 'ratingQuery.html', {"rating":output})


def tagQuery(request):
    tagVal = request.GET['tag']
    departments=apis.objects.filter(Tags__contains=tagVal)
    departments_serializer = DepartmentSerializer(departments, many=True)
    output = []
    for qrs in departments_serializer.data:
        temp = {}
        temp["id"] = str(qrs['id'])
        temp["apiId"] = qrs['apiId'] 
        temp["Tags"]  = qrs['Tags'] 
        output.append(temp)
    return render(request, 'tagQuery.html', {"tag":output})

def keywordQuery(request):
    result = []
    keyword = request.GET['keyword']
    for k in keyword.split(' '):
        k = " " + k + " "
        tempSet = set()
        queryResult = apis.objects.filter(Q(summary__contains=k) | Q(title__contains=k)| Q(description__contains=k))
        queryResult_serializer = DepartmentSerializer(queryResult, many=True)
        for item in queryResult_serializer.data:
            tempSet.add(item['id'])
        result.append(tempSet)
    unitedResult = result[0]
    for s in result[1:]:
        unitedResult.intersection_update(s)
    qualifyRecord = apis.objects.filter(id__in = unitedResult)
    qualifyRecord_serializer = DepartmentSerializer(qualifyRecord, many=True)
    output = []
    for qrs in qualifyRecord_serializer.data:
        temp = {}
        temp["id"] = str(qrs['id'])
        temp["title"] = qrs['title'] 
        temp["summary"] = qrs['summary'] 
        temp["description"]  = qrs['description'] 
        output.append(temp)
    return render(request, 'keywordQuery.html', {"keyword":output})


def updatedQueryMash(request):
    updatedYear = request.GET['updatedMash']
    departments=mashs.objects.filter(updated__startswith=updatedYear)
    departments_serializer = MashSerializer(departments, many=True)
    output = []
    for qrs in departments_serializer.data:
        temp = {}
        temp["id"] = str(qrs['id'])
        temp["apiId"] = qrs['apiId'] 
        temp["updated"]  = qrs['updated'] 
        output.append(temp)
    return render(request, 'updatedQueryMash.html', {"updated":output})


def usedAPIMash(request):
    usedAPI = request.GET['usedAPI']
    departments=mashs.objects.filter(APIs__contains=usedAPI)
    departments_serializer = MashSerializer(departments, many=True)
    output = []
    for qrs in departments_serializer.data:
        temp = {}
        temp["id"] = str(qrs['id'])
        temp["apiId"] = qrs['apiId'] 
        temp["APIs"]  = qrs['APIs'] 
        output.append(temp)
    return render(request, 'usedAPIMash.html', {"usedAPI":output})


def tagsMash(request):
    tags = request.GET['tag']
    departments=mashs.objects.filter(Tags__contains=tags)
    departments_serializer = MashSerializer(departments, many=True)
    output = []
    for qrs in departments_serializer.data:
        temp = {}
        temp["id"] = str(qrs['id'])
        temp["apiId"] = qrs['apiId'] 
        temp["Tags"]  = qrs['Tags'] 
        output.append(temp)
    return render(request, 'tagsMash.html', {"tags":output})


def keywordQueryMash(request):
    result = []
    keyword = request.GET['keyword']
    for k in keyword.split(' '):
        k = " " + k + " "
        tempSet = set()
        queryResult = mashs.objects.filter(Q(summary__contains=k) | Q(title__contains=k)| Q(description__contains=k))
        queryResult_serializer = MashSerializer(queryResult, many=True)
        for item in queryResult_serializer.data:
            tempSet.add(item['id'])
        result.append(tempSet)
    unitedResult = result[0]
    for s in result[1:]:
        unitedResult.intersection_update(s)
    qualifyRecord = mashs.objects.filter(id__in = unitedResult)
    qualifyRecord_serializer = MashSerializer(qualifyRecord, many=True)
    output = []
    for qrs in qualifyRecord_serializer.data:
        temp = {}
        temp["id"] = str(qrs['id'])
        temp["title"] = qrs['title'] 
        temp["summary"] = qrs['summary'] 
        temp["description"]  = qrs['description'] 
        output.append(temp)
    return render(request, 'keywordQueryMash.html', {"keyword":output})
    