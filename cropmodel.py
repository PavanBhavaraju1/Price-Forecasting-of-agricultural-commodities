import numpy as np
import keras
import tensorflow as tf
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

K.clear_session()


def prediction(input_value):
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    bold = '\033[1m'
    italics = '\033[3m'
    underline = '\033[4m'
    end = '\033[0m'
    input_list=[]
    input_list.append(input_value['Year'])
    input_list.append(input_value['Month'])
    input_list.append(89) #rainfall value
    
    if(input_value['District']=="Amravati"):
        input_list.append(1)
        input_list.append(0)
    elif(input_value['District']=="Ratnagiri"):
        input_list.append(0)
        input_list.append(1)
    else:
        input_list.append(0)
        input_list.append(0)
  
    
    input_list = np.array(input_list)
    input_list = input_list.reshape( (1,5) )
    input_list = np.matrix(input_list)
    json_file = open('C:\\Users\\PAVAN BHAVARAJU\\Desktop\\Price Forecasting Project\\model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    global graph
    graph=tf.compat.v1.get_default_graph()
    with graph.as_default():
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("C:\\Users\\PAVAN BHAVARAJU\\Desktop\\Price Forecasting Project\\model1.h5")

        loaded_model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])

        values=loaded_model.predict(input_list)
        del input_list
    keras.backend.clear_session()
    print(bold +red+"Your Crop WPI is Rs.",values,"perkilogram"+end)

inputs={'Year':int(input("\033[1m\033[91mYear:")),'Month':int(input("Month:")),'District':input("District:"),'Crop' :input("Crop:")} 
print("\u001b[0m----")   
prediction(inputs);
