# 简单模型
import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 忽略烦人的警告
# -1到1 构件100个数据
train_X = np.linspace(-1, 1, 100)
print(train_X)
print(train_X.shape)

train_Y = 2 * train_X + np.random.random(*train_X.shape) * 0.33 + 10

print(np.random.random(*train_X.shape))
# 类似与构件一个线性方程： y=2x+ 10+ a 类型


X = tf.placeholder("float")
print('X=', X)
Y = tf.placeholder("float")
print('Y=', Y)
W = tf.Variable(0.0, name="weight")
print('W=', W)
b = tf.Variable(0.0, name="bias")
print('b=', b)
loss = tf.square(Y - tf.multiply(X, W) - b)
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    epoch = 1
    for i in range(10):
        for (x, y) in zip(train_X, train_Y):
            _, w_value, b_value = sess.run([train_op, W, b], feed_dict={X: x, Y: y})
            print("Epoch:{},w:{},b:{}".format(epoch, w_value, b_value))
            epoch += 1
