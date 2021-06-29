import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def equation(x):
    y = (3*x) - 2
    return y

print(f"Equation value:{equation(10)}")

x = []
y = []

for z in range(0,10):
    c = equation(z)
    x.append(z)
    y.append(c)  

x = np.array(x)
y = np.array(y)

def my_model():
    model = Sequential()
    model.add(Dense(units=1,input_shape=[1]))
    return model

model = my_model()

print("Model Summary")

print(model.summary())

model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['accuracy'])

model.fit(x,y, epochs=500)

model.save("./model.h5")