import logging
import tensorflow
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start')
'''运算'''
# 定义一个占位符，类型为float64
PLACEHOLDER_A = tensorflow.placeholder(tensorflow.float64)
# 定义一个占位符，类型为float64
PLACEHOLDER_B = tensorflow.placeholder(tensorflow.float64)

# 定义一个加运算
OPERATION_ADD = tensorflow.add(PLACEHOLDER_A, PLACEHOLDER_B)

# 定义一个乘运算
OPERATION_MULTIPLY = tensorflow.multiply(PLACEHOLDER_A, PLACEHOLDER_B)

# 创建一个会话
SESSION = tensorflow.Session()
FLOAT_A = random.random()
FLOAT_B = random.random()
logging.debug('FLOAT_A : %f', FLOAT_A)
logging.debug('FLOAT_B : %f', FLOAT_B)
logging.debug('OPERATION_ADD(float_a, float_b) : %f', SESSION.run(OPERATION_ADD, feed_dict={PLACEHOLDER_A: FLOAT_A, PLACEHOLDER_B: FLOAT_B}))
logging.debug('OPERATION_MULTIPLY(float_a, float_b) : %f', SESSION.run(OPERATION_MULTIPLY, feed_dict={PLACEHOLDER_A: FLOAT_A, PLACEHOLDER_B: FLOAT_B}))
