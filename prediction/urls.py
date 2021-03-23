from django.urls import path

from . import views

urlpatterns = [
    path('result/', views.prediction_result, name='result'),
    path('patient-list/', views.patient_list, name='patient-list')
]
