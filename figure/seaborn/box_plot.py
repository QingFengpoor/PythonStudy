#!/usr/bin/python3
#encoding: utf-8
'''
@File    :   Main.py
@Time    :   2020/06/13 22:21:34
@Author  :   Qingfeng
@Version :   1.0
@Contact :   2267647906@qq.com
'''

# to show figure. UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
import matplotlib
#matplotlib.use('nbAgg')
matplotlib.use('Qt5Agg')

# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
 
def box_plot():
    # Dataset:
    a = pd.DataFrame({ 'group' : np.repeat('A',500), 'value': np.random.normal(10, 5, 500) })
    b = pd.DataFrame({ 'group' : np.repeat('B',500), 'value': np.random.normal(13, 1.2, 500) })
    c = pd.DataFrame({ 'group' : np.repeat('B',500), 'value': np.random.normal(18, 1.2, 500) })
    d = pd.DataFrame({ 'group' : np.repeat('C',20), 'value': np.random.normal(25, 4, 20) })
    e = pd.DataFrame({ 'group' : np.repeat('D',100), 'value': np.random.uniform(12, size=100) })
    df=a.append(b).append(c).append(d).append(e)

    widths = [1, 1]
    heights = [1, 1]

    gs_kw = dict(width_ratios=widths, height_ratios=heights)
    f, axs = plt.subplots(nrows=2, ncols=2, constrained_layout=True, gridspec_kw=gs_kw)
    f.canvas.set_window_title("Boxplot")
    # Usual boxplot
    ax = sns.boxplot(x='group', y='value', data=df, ax=axs[0, 0])
    ax.set_title("Ususal boxplot")


    # add Jitter
    ax = sns.boxplot(x='group', y='value', data=df, ax=axs[0, 1])
    ax = sns.stripplot(x='group', y='value', data=df, color="orange", jitter=0.2, size=2.5, ax=axs[0, 1])
    ax.set_title("Boxplot with jitter", loc="left")


    # violin plot
    ax = sns.violinplot( x='group', y='value', data=df, ax=axs[1, 0])
    ax.set_title("Violin plot", loc="left")


    # show number of obs
    # Start with a basic boxplot
    ax = sns.boxplot(x="group", y="value", data=df, ax=axs[-1, -1])
    
    # Calculate number of obs per group & median to position labels
    medians = df.groupby(['group'])['value'].median().values
    nobs = df.groupby("group").size().values
    nobs = [str(x) for x in nobs.tolist()]
    nobs = ["n: " + i for i in nobs]
    
    # Add it to the plot
    pos = range(len(nobs))
    for tick,label in zip(pos,ax.get_xticklabels()):
        ax.text(pos[tick], medians[tick] + 0.4, nobs[tick], horizontalalignment='center', size='medium', color='w', weight='semibold')
    
    # add title
    ax.set_title("Boxplot with number of observation", loc="left")

    plt.show()
    plt.close()


if __name__ == "__main__":
    box_plot()