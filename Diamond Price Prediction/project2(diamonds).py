# -*- coding: utf-8 -*-
"""Project2(Diamonds).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11pcFp27Kg4qnp26fnAp02UuO-aWGfV1o
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
data = pd.read_csv("diamonds.csv")

#Analyse data
data.info()
data.head()

#Remove unnecessary column
data.drop(['Unnamed: 0'], axis=1, inplace=True)

import numpy as np
from sklearn.model_selection import train_test_split

#data_features = data.copy()
data_features = data.drop(['price'], axis=1)
data_labels = data['price']

data_features.info()

from sklearn.preprocessing import OrdinalEncoder, StandardScaler

#use ordinal encoder to categorize more than two object 
cut_categories = ['Fair','Good','Very Good','Premium','Ideal']
color_categories = ['J','I','H','G','F','E','D']
clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
encod = OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])

data_features[['cut','color','clarity']] = encod.fit_transform(data_features[['cut','color','clarity']])

import numpy as np
from sklearn.model_selection import train_test_split

SEED = 123
#split data into train_validation_test set
x_train,x_vtest,y_train,y_vtest = train_test_split(data_features, data_labels, test_size=0.4, random_state=SEED)
x_val,x_test,y_val,y_test = train_test_split(x_vtest, y_vtest, test_size=0.5, random_state=SEED)

#feature scaling for fitting
scaler = StandardScaler()
scaler.fit(x_train)
scaler.transform(x_train)
scaler.transform(x_val)
scaler.transform(x_test)

#create FNN using Tensorflow Keras

import tensorflow as tf

model = tf.keras.Sequential()

model.add(tf.keras.Input(shape=(x_train.shape[-1],)))
model.add(tf.keras.layers.Dense(128,activation='elu', kernel_regularizer=tf.keras.regularizers.l2(l2=0.01)))
model.add(tf.keras.layers.Dense(64,activation='elu', kernel_regularizer=tf.keras.regularizers.l1(l1=0.05)))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(32,activation='elu', kernel_regularizer=tf.keras.regularizers.l1(l1=0.05)))
model.add(tf.keras.layers.Dense(16,activation='elu', kernel_regularizer=tf.keras.regularizers.l2(l2=0.01)))
model.add(tf.keras.layers.Dense(1))

#compile model
model.compile(optimizer='adam', loss='mse',metrics=['mse','mae'])

#visualize the keras sequential model
model.summary()
tf.keras.utils.plot_model(model, show_shapes=True, show_layer_names=True, show_layer_activations=True)

#open tensorboard and save in directory
log_dir="logs/fit/"
tb_callback=tf.keras.callbacks.TensorBoard(log_dir=log_dir)
es_callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss',patience=3,verbose=1,mode='min')

#train model
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), batch_size=60, epochs=100, callbacks=[tb_callback, es_callback])

#Evaluate the result 
test_result = model.evaluate(x_test,y_test,batch_size=40)
print(f"Test loss = {test_result[0]}")
print(f"Test mse = {test_result[1]}")
print(f"Test mae = {test_result[2]}")

# Commented out IPython magic to ensure Python compatibility.
#open and display tensorboard
# %reload_ext tensorboard
# %tensorboard --logdir logs

#plot graph predictions vs labels
import matplotlib.pyplot as plt
import os
predictions = np.squeeze(model.predict(x_test))
labels = np.squeeze(y_test)
plt.plot(predictions,labels,".")
plt.xlabel("Predictions")
plt.ylabel("Labels")
plt.title("Graph of Predictions vs Labels with Test Data")
save_path = "/content/logs"
plt.savefig(os.path.join(save_path,"result.png"),bbox_inches='tight')
plt.show()