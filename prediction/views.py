from .models import Patient
from random import *
import numpy as np
from PIL import Image
from .forms import PatientForm
import math as mt
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from numpy import asarray
from .forms import PatientForm


def prediction_result(request):
    if request.method == "POST":
        pat = Patient()
        pat.first_name = request.POST.get('f')
        pat.last_name = request.POST.get('l')
        pat.mail = request.POST.get('m')
        pat.address = request.POST.get('a')
        pat.gender = request.POST.get('gen')
        pat.dob = request.POST.get('dub')
        pat.image_file = request.POST.get('imf')
        pat.note = request.POST.get('n')

        img2 = pat.image_file
        img2 = asarray(Image.open(img2))
        print(img2)
        keras_mode = [0, 1]
        model_tensor = sample(keras_mode, 1)
        print(model_tensor)
        model_path = "keras/my_model.h5"
        pat.prediction_result = round(model_tensor[0])

        pat.save()
        return redirect('patient-list')

        # After submit button might have been clicked it redirects to a list of predicted patients

    return render(request, 'patient/patient-predict.html')


def patient_list(request, template_name='patient/patient-list.html'):
    patient = Patient.objects.all()
    pat = Patient()
    paginator = Paginator(patient, 5)
    result = pat.prediction_result
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template_name, {'object_list': patient, 'page_obj': page_obj, 'test': result})
