#!/usr/bin/python3
#encoding: utf-8
'''
@File    :   scatter_plot.py
@Time    :   2020/06/16 10:38:01
@Author  :   Qingfeng 
@Version :   1.0
@Contact :   2267647906@qq.com
'''

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd

def scatter_plot():
    # Create a dataset:
    df=pd.DataFrame({'x_value': range(1,101), 'y_value': np.random.randn(100)*15+range(1,101) })

    # figure1
    fig, ax=plt.subplots()
    fig.canvas.set_window_title("Scatter: basic")
    # plot
    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', marker='o')
    ax.set_title("Basic scatter plot")

    plt.show()
    plt.close(fig=fig)


    # figure2
    fig, ax=plt.subplots()
    fig.canvas.set_window_title("Scatter: marker shape")
    all_poss=['.','o','v','^','>','<','s','p','*','h','H','D','d','1','','']

    # to see all possibilities:
    # markers.MarkerStyle.markers.keys()

    # set the limit of x and y axis:
    ax.set_xlim(0.5,4.5)
    ax.set_ylim(0.5,4.5)

    # remove ticks and values of axis:
    ax.set_xticks([])
    ax.set_yticks([])
    #plt.set_xlabel(size=0)

    # Make a loop to add markers one by one
    num=0
    for x in range(1,5):
        for y in range(1,5):
            num += 1
            ax.plot(x,y,marker=all_poss[num-1], markerfacecolor='orange', markersize=23, markeredgecolor="black")
            ax.text(x+0.2, y, all_poss[num-1], horizontalalignment='left', size='medium', color='black', weight='semibold')

    ax.set_title("marker shape")

    plt.show()
    plt.close()


    # figure3
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("Scatter: marker size")

    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', marker='D', markersize=16)
    ax.set_title("marker size")

    plt.show()
    plt.close()


    # figure4
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("Scatter: marker color")

    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', markerfacecolor='skyblue', marker="o", markeredgecolor="black", markersize=16)
    ax.set_title("marker color")

    plt.show()
    plt.close()


    # figure5
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("Scatter: marker edge")

    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', marker='D', markersize=16, markeredgecolor="orange", markeredgewidth=5)
    ax.set_title("marker edge")
    plt.show()
    plt.close()

if __name__ == "__main__":
    scatter_plot()
