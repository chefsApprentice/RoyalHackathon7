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
# Suppress all warnings
import warnings
warnings.filterwarnings('ignore')

# Set random seeds for randomize operations in numpy as well as tensorflow
np.random.seed(30)
tf.random.set_seed(30)

# Additional cleanup for backend setup
K = tf.keras.backend #Creates alias K for tf.keras.backend module
K.set_image_data_format('channels_last') #data format is dimensions (x,y) then number of channels eg: (64,64,3)
