import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 忽略烦人的警告

hello_op = tf.constant('Hello,TensorFlow')

a = tf.constant(10)
b = tf.constant(32)
compute_op = tf.add(a, b)

with tf.Session() as sess:
    print(sess.run(hello_op))
    print(sess.run(compute_op))
