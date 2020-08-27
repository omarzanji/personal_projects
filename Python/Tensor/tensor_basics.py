# Basics from tensorflow.org/data
#
#

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.set_printoptions(precision=4)


# To create input pipeline, need a dataset:
dataset = tf.data.Dataset.from_tensor_slices([8,3,0,8,2,1])

# To iterate:
print("iterating through dataset: ")
for elem in dataset:
    print(elem.numpy())
