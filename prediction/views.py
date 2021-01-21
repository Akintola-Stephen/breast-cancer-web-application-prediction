import keras
from keras.utils.np_utils import to_categorical
from django.shortcuts import render
from .forms import PatientForm
import cv2

import numpy as np

def prepare(path):
    img_size = 1146
    img_array = cv2.imread(path,)




def prediction_result(request):
    form = PatientForm(request.POST or None , request.FILES or None )
    if form.is_valid():
        instance = form.save(commit=False)

        #img_var =  np.asarray(form.cleaned_data['image_file'])
        img_var = request.FILES.get(   'image_file')
        keras_saved_model = 'keras-model/my_model.h5'
        model = keras.models.load_model(keras_saved_model)

        prediction = model.predict(
                [img_var]
        )

        instance.prediction_result = int(prediction[0])
        instance.save()

        if int(prediction[0]) == 1:
                value = "have"

    context = {
                'form': form
    }
    return render(request, 'patient/patient-predict.html', context)



def patient_list():
    pass