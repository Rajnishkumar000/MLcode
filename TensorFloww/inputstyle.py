import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import keras

from tensorflow.python.keras import Input

image_dimensions = {'height':256, 'width':256, 'channels':3}

x = Input(shape=(image_dimensions['height'],
                 image_dimensions['width'],
                 image_dimensions['channels']))

print(x)