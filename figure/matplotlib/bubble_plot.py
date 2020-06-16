#!/usr/bin/python3
#encoding: utf-8
'''
@File    :   bubble_plot.py
@Time    :   2020/06/16 10:37:32
@Author  :   Qingfeng 
@Version :   1.0
@Contact :   2267647906@qq.com
'''

# select backen
import matplotlib
matplotlib.use("Qt5Agg")
# libraries
import matplotlib.pyplot as plt
import numpy as np

def buble_plot():
    # create data
    x = np.random.rand(40)
    y = np.random.rand(40)
    z = np.random.rand(40)
    

    # figure 1
    fig, ax = plt.subplots()
    fig.canvas.set_window_title('Bubble Plot')
    # use the scatter function
    ax.scatter(x, y, s=z*1000, alpha=0.5)
    ax.set_title("Basic bubble plot")

    plt.show()
    plt.close()


    # figure 2
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("Buble Plot")
    y = x+np.random.rand(40)
    z = x+np.random.rand(40)
    z=z*z
    
    # Change color with c and alpha. I map the color to the X axis value.
    ax.scatter(x, y, s=z*2000, c=x, cmap="Blues", alpha=0.4, edgecolors="grey", linewidth=2)
    
    # Add titles (main and on axis)
    ax.set_xlabel("the X axis")
    ax.set_ylabel("the Y axis")
    ax.set_title("A colored bubble plot")
    
    plt.show()
    plt.close()



if __name__ == "__main__":
    buble_plot()
