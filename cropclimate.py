import numpy as np
import keras
import tensorflow as tf
from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

K.clear_session()

def climate(input_numbers):

    input_list=[]
    input_list.append(input_numbers['Air_Temp'])
    input_list.append(input_numbers['Air_Humidity'])
    input_list.append(89)  # rainfall value
    print(input_list)
    if (input_numbers['label'] == "rice"):
        input_list.append(1)
        input_list.append(0)
    # elif (input_numbers['Soil_ph'] < 5):
    #     input_list.append(0)
    #     input_list.append(1)
    else:
        input_list.append(0)
        input_list.append(1)
    print(input_list)



    input_list = np.array(input_list)
    input_list = input_list.reshape((1, 5))
    input_list = np.matrix(input_list)

    json_file = open('C:\\Users\\PAVAN BHAVARAJU\\Desktop\\Price Forecasting Project\\modelc.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    global graph
    graph = tf.compat.v1.get_default_graph()
    with graph.as_default():
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("C:\\Users\\PAVAN BHAVARAJU\\Desktop\\Price Forecasting Project\\modelcli.h5")

        loaded_model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])

        values = loaded_model.predict(input_list)
        del input_list
    keras.backend.clear_session()
    return values
