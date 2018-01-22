import logging
import random

import tensorflow

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start')


'''矩阵乘法'''

# 定义一个1x2的矩阵常量
MATRIX_LEFT = tensorflow.constant([[random.random(), random.random()]])

# 定义一个2x1的矩阵常量
MATRIX_RIGHT = tensorflow.constant([[random.random()],
                                    [random.random()]])

# 1x2的矩阵乘2x1的矩阵
PRODUCT_LEFT_RIGHT = tensorflow.matmul(MATRIX_LEFT, MATRIX_RIGHT)

# 2x1的矩阵乘1x2的矩阵
PRODUCT_RIGHT_LEFT = tensorflow.matmul(MATRIX_RIGHT, MATRIX_LEFT)

# 创建一个会话
SESSION = tensorflow.Session()

# 显示1x2矩阵
logging.debug('MATRIX_LEFT : \n%s', SESSION.run(MATRIX_LEFT))

# 显示2x1矩阵
logging.debug('MATRIX_RIGHT : \n%s', SESSION.run(MATRIX_RIGHT))


# 显示1x2的矩阵乘2x1的矩阵的结果，是1x1矩阵
logging.debug('MATRIX_LEFT x MATRIX_RIGHT : \n%s', SESSION.run(PRODUCT_LEFT_RIGHT))
# 显示2x1的矩阵乘1x2的矩阵的结果，是2x2矩阵
logging.debug('MATRIX_RIGHT x MATRIX_LEFT : \n%s', SESSION.run(PRODUCT_RIGHT_LEFT))
