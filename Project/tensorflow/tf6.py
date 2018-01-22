# 回归
import logging
import os

import matplotlib.pyplot as mp
import numpy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start tensorflow tutorial example 6 least squares')

STR_SCRIPT_DIR, STR_SCRIPT_FILE = os.path.split(__file__)
# 得到当前目录
logging.debug('STR_SCRIPT_DIR : %s', STR_SCRIPT_DIR)
# 获取文件名 xx.py
logging.debug('STR_SCRIPT_FILE : %s', STR_SCRIPT_FILE)
# 取文件名 xx
STR_SCRIPT_PREFIX = os.path.splitext(STR_SCRIPT_FILE)[0]
logging.debug('STR_SCRIPT_PREFIX : %s', STR_SCRIPT_PREFIX)
# os.path.join(STR_SCRIPT_DIR, STR_SCRIPT_PREFIX + '.ext')
# 样本x
SAMPLE_X = numpy.asarray([474.7, 479.9, 488.1, 509.6, 576.4, 654.7, 755.6,
                          798.6, 815.4, 718.4, 767.2, 759.5, 820.3, 849.8,
                          974.7, 1041.0, 1099.3, 1186.1, 1252.5])
logging.debug('SAMPLE_X : \n%s', SAMPLE_X)
# 样本y
SAMPLE_Y = numpy.asarray([526.9, 532.7, 566.8, 591.2, 700.0, 744.1, 851.2,
                          884.4, 847.3, 821.0, 884.2, 903.7, 984.1, 1035.3,
                          1200.9, 1289.8, 1432.9, 1539.0, 1663.6])
logging.debug('SAMPLE_Y : \n%s', SAMPLE_Y)
# 样本数量
N_SAMPLES = SAMPLE_X.shape[0]
logging.debug('N_SAMPLES : %d', N_SAMPLES)
# 样本x的平均值
MEAN_X = sum(SAMPLE_X) / N_SAMPLES
logging.debug('MEAN_X : %f', MEAN_X)
# 样本y的平均值
MEAN_Y = sum(SAMPLE_Y) / N_SAMPLES
logging.debug('MEAN_Y : %f', MEAN_Y)
# 权重
WEIGHT = ((sum(SAMPLE_X[i] * SAMPLE_Y[i] for i in range(N_SAMPLES)) - N_SAMPLES * MEAN_X * MEAN_Y) /
          sum((SAMPLE_X[i] - MEAN_X) * (SAMPLE_X[i] - MEAN_X) for i in range(N_SAMPLES)))
logging.debug('WEIGHT : %f', WEIGHT)
# 偏置
BIAS = MEAN_Y - WEIGHT * MEAN_X
logging.debug('BIAS : %f', BIAS)
# 绘制样本
mp.plot(SAMPLE_X, SAMPLE_Y, 'ro', label='样本')
# 绘制拟合直线
mp.plot(SAMPLE_X, SAMPLE_X * WEIGHT + BIAS, label='拟合')
# 显示图例
mp.legend()
# 保存图片
mp.savefig(os.path.join(STR_SCRIPT_DIR, STR_SCRIPT_PREFIX + '.png'))
# 显示图片
mp.show()
