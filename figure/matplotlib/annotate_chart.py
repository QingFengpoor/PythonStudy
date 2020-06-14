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

    plt.show()
    plt.close()

    import matplotlib.patches as patches
    # figure 2
    fig, ax = plt.subplots()
    


if __name__ == "__main__":
    annotate_chart()
