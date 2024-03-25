from django.shortcuts import render, redirect
import tensorflow as tf
from django.http import HttpResponse, HttpRequest
import os
from django.conf import settings
import base64
from tensorflow.keras.applications.imagenet_utils import preprocess_input , decode_predictions
from tensorflow.keras.models import load_model
from threading import Timer



def load_the_model_once(): 
    global my_model 
    #my_model = load_model(os.path.join(settings.BASE_DIR, 'model.h5'))
    my_model = load_model(os.path.join(settings.STATIC_ROOT, 'model.h5'))
   

def redirect_home(request):
    loading_model = Timer(1.0, load_the_model_once)
    loading_model.start()
    
    
    response = redirect(home)
    return response


def redirectio(request):  
    response = redirect(home)
    return response

def  home(request) :
    return render(request, 'index.html')

def transform_img(img) :
    s = base64.b64encode(img.read())
    return s.decode('utf-8')

def traiter_image(img):
    link_of_image=img
    image = tf.keras.preprocessing.image.load_img(link_of_image, target_size=(224, 224))  
    image = tf.keras.preprocessing.image.img_to_array(image) 
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2])) 
    image = tf.keras.applications.vgg19.preprocess_input(image) 
    return image



def classification(request,img) : 
    image = traiter_image(img)
    vgg19 = my_model
    preds = vgg19.predict(image)
    Top_predictions = decode_predictions(preds, top = 3)
        
    prediction1 = Top_predictions[0][0][1]
    prediction2 = Top_predictions[0][1][1]
    prediction3 = Top_predictions[0][2][1]

    prob1 = round(float(Top_predictions[0][0][2])*100,2)
    prob2 = round(float(Top_predictions[0][1][2])*100,2)
    prob3 = round(float(Top_predictions[0][2][2])*100,2)

    return prediction1,prediction2,prediction3, prob1,prob2,prob3


def get_image(request) :
    if request.method == 'POST' :
        
        image=request.FILES['img'].file
        img= transform_img(request.FILES['img'])     
       
        predict1,predict2,predict3, prob1,prob2,prob3 = classification(request, image)
        return render(request, 'classer.html',
         context={
            'image' : img,
         'predict1' : predict1,
          'predict2' :predict2,
          'predict3' :predict3,
         'prob1' : prob1,
          'prob2' :prob2,
          'prob3' :prob3
         })
        







