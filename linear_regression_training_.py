import pickle

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

with open("theta.pkl","rb") as f:
    theta_val = pickle.load(f)


def predict_marks(x, theta_val = theta_val):
    return hypothesis(x,theta_val)


def hypothesis(x,theta):
    y_ = theta[0] + theta[1]*x
    return y_