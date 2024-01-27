import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from imageio import imread
from skimage.transform import resize
import datetime
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Flatten, TimeDistributed, BatchNormalization, Activation, Dropout, SimpleRNN, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras import optimizers

import warnings
warnings.filterwarnings('ignore')

np.random.seed(30)
tf.random.set_seed(30)

K = tf.keras.backend #Creates alias K for tf.keras.backend module
K.set_image_data_format('channels_last') #data format is dimensions (x,y) then number of channels eg: (64,64,3)

project_folder=r'C:\Users\quinb\Desktop\Thumbs_up_and_down_Dataset'
read = pd.read_csv(r'C:\Users\quinb\Desktop\Thumbs_up_and_down_Dataset\train.csv',dtype=object)
print(read.shape) #shape of a DataFrame is a tuple ( no of rows, no of columns)
print(read.info())
#rrrr
