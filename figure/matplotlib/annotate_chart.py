import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd

def annotate_chart():
    df=pd.DataFrame({'x_value': range(1,101), 'y_value': np.random.randn(100)*15+range(1,101) })

    # #显示所有列
    # pd.set_option('display.max_columns', None)
    # #显示所有行
    # pd.set_option('display.max_rows', None)
    # print(df)

    # figure 1
    fig, ax = plt.subplots()
    # Basic chart
    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', marker='o')
    
    print("xy=(%d, %d)"%(df.iat[25, 0],df.iat[25, 1]))

    # Annotate with text + Arrow
    ax.annotate(
    # Label and coordinate
    'This point is interesting!', xy=(df.iat[25, 0],df.iat[25, 1]), xytext=(0, 80),
    
    # Custom arrow
    arrowprops=dict(facecolor='black', shrink=0.05)
    )
    ax.set_title("text & custom arrow")

    plt.show()
    plt.close()


    import matplotlib.patches as patches
    # figure 2
    fig, ax = plt.subplots()

    # Plot
    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', marker='o')
    
    # Add rectangle
    ax.add_patch(
    patches.Rectangle(
    (df.iat[25, 0],df.iat[25, 1]), # (x,y) left_bottom
    50, # width
    50, # height
    # You can add rotation as well with 'angle'
    alpha=0.3, facecolor="red", edgecolor="black", linewidth=3, linestyle='solid'
    )
    )
    ax.set_title("rectangle patch")

    plt.show()
    plt.close()


    # figure3
    fig, ax = plt.subplots()

    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', marker='o')
 
    # Annotation
    ax.add_patch(
    patches.Circle(
    (df.iat[25, 0],df.iat[25, 1]),           # (x,y), the center
    30,                    # radius
    alpha=0.3, facecolor="green", edgecolor="black", linewidth=1, linestyle='solid'
    )
    )
    ax.set_title("circle patch")

    plt.show()
    plt.close()


    # figure 4
    fig, ax = plt.subplots()

    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', marker='o')
    ax.add_patch(
    patches.Ellipse(
    (df.iat[25, 0],df.iat[25, 1]), # (x,y)
    30, # width
    100, # height
    45, # radius
    alpha=0.3, facecolor="green", edgecolor="black", linewidth=1, linestyle='solid'
    )
    )
    ax.set_title("ellipse patch")

    plt.show()
    plt.close()


    # figure 5
    fig, ax = plt.subplots()
    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', marker='o')

    # Annotation 
    ax.plot([80, 40], [30, 90], color="skyblue", lw=5, linestyle='solid', label="_not in legend")
    ax.set_title("segment, acturally straight line")

    plt.show()
    plt.close()


    # figure 6
    fig, ax = plt.subplots()

    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', marker='o')
    
    # Annotation
    ax.axvline(df.iat[25, 0], color='r')
    ax.axhline(df.iat[25, 1], color='green')
    ax.set_title("vertical and horizental lines")

    plt.show()
    plt.close()


    # figure 7
    fig, ax = plt.subplots()

    ax.plot( 'x_value', 'y_value', data=df, linestyle='none', marker='o')
    
    # Annotation
    ax.text(40, 00, r'equation: $\sum_{i=0}^\infty x_i$', fontsize=20)
    ax.set_title("math, by text with content of equation")

    plt.show()
    plt.close()



if __name__ == "__main__":
    annotate_chart()
