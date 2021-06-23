from .serializers import EmpPersonalSerializers, EmpProfessionSerializers,\
     EmployeeSerializers,EmpDesignationSerializers,\
    EmpAddressSerializers,EmployeeProfession
from .models import EmployeeModel,EmployeeDesignation,\
    EmployeeAddress, EmployeePersonalDetails,EmployeeProfession
from rest_framework import  viewsets


class Employee(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializers

class Employee_Designation(viewsets.ModelViewSet):
    queryset = EmployeeDesignation.objects.all()
    serializer_class = EmpDesignationSerializers


class Employee_Address(viewsets.ModelViewSet):
    queryset = EmployeeAddress.objects.all()
    serializer_class = EmpAddressSerializers

class Employee_Profession(viewsets.ModelViewSet):
    queryset = EmployeeProfession.objects.all()
    serializer_class = EmpProfessionSerializers

class Emmployee_Personal(viewsets.ModelViewSet):
    queryset = EmployeePersonalDetails.objects.all()
    serializer_class = EmpPersonalSerializers