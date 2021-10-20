import numpy as np
import matplotlib.pyplot as plt
import traceback
import matplotlib.gridspec as gridspec
from matplotlib import rcParams
import matplotlib.ticker as ticker
import datetime
from scipy.fftpack import fft
from math import  pi
    
data_k = np.loadtxt("data.txt", dtype = float)
data = np.loadtxt("data.txt", dtype = int)

data = data*4/255
P_A = len(data)
fig_data = plt.figure()

x_A = list(range(0, P_A))
x_A = [i/100 for i in x_A]

subplot_data_R = fig_data.add_subplot(111)

subplot_data_R.set_ylabel('Напряжение, В')
subplot_data_R.set_xlabel('Время, с')

subplot_data_R.set_title('Зависимость напряжение от времени')

line_data_R = subplot_data_R.plot(x_A, data, marker = '*', color='brown', linewidth=2, label='напряжение', markevery=30)
subplot_data_R.legend()
plt.show()