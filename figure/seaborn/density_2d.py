#!/usr/bin/python3
#encoding: utf-8
'''
@File    :   density_2d.py
@Time    :   2020/06/16 10:39:39
@Author  :   Qingfeng 
@Version :   1.0
@Contact :   2267647906@qq.com
'''
# use Qt5Agg
import matplotlib
matplotlib.use("Qt5Agg")
# library
import matplotlib.pyplot as plt
import seaborn as sns

def density_2d():
    # dataset
    df = sns.load_dataset('iris')

    # figure 1
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("2D-Density: Basic")

    # Basic 2D density plot
    sns.set_style("white")
    ax = sns.kdeplot(df.sepal_width, df.sepal_length)
    ax.set_title("Basic 2D density plot")
    #sns.plt.show()

    plt.show()
    plt.close()
    
    # figure 2
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("2D-Density: 1D density")

    # Custom it with the same argument as 1D density plot
    ax = sns.kdeplot(df.sepal_width, df.sepal_length, cmap="Reds", shade=True, bw=.15)
    ax.set_title("2D-Density: cmap='Reds', (kernel size)bw=.15")
    #sns.plt.show()

    plt.show()
    plt.close()
    
    # figure 3
    fig, ax = plt.subplots()
    fig.canvas.set_window_title("2D-Density: color the lowest")

    # Some features are characteristic of 2D: color palette and wether or not color the lowest range
    ax = sns.kdeplot(df.sepal_width, df.sepal_length, cmap="Blues", shade=True, shade_lowest=True, )
    ax.set_title("cmap='Blues', shade")
    #sns.plt.show()

    plt.show()
    plt.close()


if __name__ == "__main__":
    density_2d()
