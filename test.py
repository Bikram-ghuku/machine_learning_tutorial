from re import X
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model("./model.h5")

def model_equation(d):
    o = model.predict([int(d)])
    return o

def equation(x):
    y = (3*x) - 2
    return y

def compare_data_V1(u):
    equation_data = equation(u)
    model_data = model_equation(u)[0][0]
    difference = equation_data - model_data
    print(f"Equation value(Ground Thruth): {equation_data} \n Model Data(Predicted): {model_data} \n Difference between ground truth and predicted data: {difference}")

while True:
    x = int(input("Enter Number: "))
    compare_data_V1(x)