import json
from http import HTTPStatus
from http.client import responses

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee


def employee(request):
    return  HttpResponse("hello django")

@csrf_exempt
def add_employee(request):
    if request.method=='POST':
        data=json.loads(request.body)

        emp_data = Employee.objects.create(
            employee_id =data.get("employee_id"),
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            address=data.get("address"),
            salary=data.get("salary")
        )
        return JsonResponse({
            "data":emp_data.employee_id,
            "status":HTTPStatus.OK
        })
        return HttpResponse("done")


def get_employee_details(request):
    emp_data=Employee.objects.all().values()
    response_data=list(emp_data)
    return JsonResponse({
        "data":response_data
    })

