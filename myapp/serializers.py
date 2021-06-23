from rest_framework import serializers
from myapp.models import EmployeeModel,EmployeeDesignation,EmployeeAddress,\
    EmployeeProfession,EmployeePersonalDetails

class EmpPersonalSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeePersonalDetails
        fields = "__all__"

class EmpProfessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfession
        fields = "__all__"

class EmpDesignationSerializers(serializers.ModelSerializer):
    profession = EmpProfessionSerializers(many=True,read_only=True)
    class Meta:
        model = EmployeeDesignation
        fields = "__all__"

class EmpAddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAddress
        fields = "__all__"

class EmployeeSerializers(serializers.ModelSerializer):
    designation = EmpDesignationSerializers(many=True,read_only=True)
    address = EmpAddressSerializers(many=True,read_only=True)
    personal_details = EmpPersonalSerializers(many=True,read_only=True)
    class Meta:
        model = EmployeeModel
        fields = "__all__"
    
