from django.db import router
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('Employee',views.Employee,basename="employee")
router.register('Employee_Designation',views.Employee_Designation,basename='designation')
router.register('Employee_Address',views.Employee_Address,basename="address")
router.register('Profession',views.Employee_Profession,basename="profession")
router.register('Personal_details',views.Emmployee_Personal,basename='personal'),


urlpatterns = [
    path('',include(router.urls)),
]
