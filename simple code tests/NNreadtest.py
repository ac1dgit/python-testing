import numpy as np
import tensorflow as tf

# example from tensorflow.org

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.load_model('testmodel.h5')
model.evaluate(x_test, y_test)