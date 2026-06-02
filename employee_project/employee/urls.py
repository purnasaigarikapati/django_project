from .views import employee,add_employee,get_employee_details
from django.urls import path

urlpatterns = [

    path('sai/',employee),
    path('sss/',add_employee),
    path('satish/',get_employee_details)
]