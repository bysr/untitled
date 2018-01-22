import logging
import tensorflow
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start')
'''算数'''
# 定义一个常数 CONSTANT_A
CONSTANT_A = tensorflow.constant(random.randint(-100, 100))
# 定义一个常数 CONSTANT_B
CONSTANT_B = tensorflow.constant(random.randint(-100, 100))

# 创建一个回话
SESSION = tensorflow.Session()

# 输出 CONSTANT_A
logging.debug('CONSTANT_A = %s', SESSION.run(CONSTANT_A))
# 输出 CONSTANT_B
logging.debug('CONSTANT_B = %s', SESSION.run(CONSTANT_B))
# 计算 CONSTANT_A + CONSTANT_B
logging.debug('CONSTANT_A + CONSTANT_B = %s', SESSION.run(CONSTANT_A + CONSTANT_B))
# 计算 CONSTANT_A * CONSTANT_B
logging.debug('CONSTANT_A * CONSTANT_B = %s', SESSION.run(CONSTANT_A * CONSTANT_B))
