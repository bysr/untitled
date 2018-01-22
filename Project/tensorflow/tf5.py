
import logging
import random

import tensorflow

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start tensorflow tutorial example 5 matrix multiply operation')
'''
矩阵乘法运算
'''

# 定义一个占位符矩阵，类型为float64，尺寸为一行两列
PLACEHOLDER_A = tensorflow.placeholder(tensorflow.float64, [1, 2])


# 定义一个占位符矩阵，类型为float64，尺寸为两行一列
PLACEHOLDER_B = tensorflow.placeholder(tensorflow.float64, [2, 1])

# 定义一个矩阵乘法运算，左A右B
OPERATION_MATMUL_A_B = tensorflow.matmul(PLACEHOLDER_A, PLACEHOLDER_B)

# 定义一个矩阵乘法运算，左B右A
OPERATION_MATMUL_B_A = tensorflow.matmul(PLACEHOLDER_B, PLACEHOLDER_A)
# 创建一个会话
SESSION = tensorflow.Session()

# 一个尺寸为一行两列的矩阵
MATRIX_A = [[random.random(), random.random()]]
# 一个尺寸为两行一列的矩阵
MATRIX_B = [[random.random()],
            [random.random()]]

# 显示尺寸为一行两列的矩阵的值
logging.debug('MATRIX_A : \n%s', MATRIX_A)
# 显示尺寸为两行一列的矩阵的值
logging.debug('MATRIX_B : \n%s', MATRIX_B)

# 运行左A右B的矩阵乘法运算，结果是1x1矩阵
logging.debug('OPERATION_MATMUL_A_B(PLACEHOLDER_A, PLACEHOLDER_B) : \n%s', SESSION.run(OPERATION_MATMUL_A_B, feed_dict={PLACEHOLDER_A: MATRIX_A, PLACEHOLDER_B: MATRIX_B}))
# 运行左B右A的矩阵乘法运算，结果是2x2矩阵
logging.debug('OPERATION_MATMUL_B_A(PLACEHOLDER_A, PLACEHOLDER_B) : \n%s', SESSION.run(OPERATION_MATMUL_B_A, feed_dict={PLACEHOLDER_A: MATRIX_A, PLACEHOLDER_B: MATRIX_B}))

