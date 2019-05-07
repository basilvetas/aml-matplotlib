from os.path import join, dirname, realpath
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

path = realpath(join(dirname(__file__), 'mpg.csv'))
df = pd.read_csv(path);

def overlapping_plot(kwargs):
  """ Reproduces the graphs on overlapping data from "Fundamentals of Data Visualization" """

  df_fwd = df.loc[df.drv == 'f']
  df_rwd = df.loc[df.drv == 'r']
  df_4wd = df.loc[df.drv == '4']
  x1 = df_fwd.displ
  x2 = df_rwd.displ
  x3 = df_4wd.displ
  y1 = df_fwd.cty
  y2 = df_rwd.cty
  y3 = df_4wd.cty

  # create layout
  fig, axes = plt.subplots(2, 2, figsize=(10,10))

  for i in[0,1]:
    for j in [0,1]:

      if i == 1 or j == 1:
        # transparency
        kwargs['alpha'] = .5

      if i == 1 and j == 0:
        # a bit of jitter
        x1 = x1.apply(lambda x: np.random.normal(x, .1))
        x2 = x2.apply(lambda x: np.random.normal(x, .1))
        x3 = x3.apply(lambda x: np.random.normal(x, .1))
      elif i == 1 and j == 1:
        # too much jitter
        x1 = x1.apply(lambda x: np.random.normal(x))
        x2 = x2.apply(lambda x: np.random.normal(x))
        x3 = x3.apply(lambda x: np.random.normal(x))

      axes[i][j].scatter(x1, y1, color='#DE8E08', label='FWD', **kwargs)
      axes[i][j].scatter(x2, y2, color='#48A4E2', label='RWD', **kwargs)
      axes[i][j].scatter(x3, y3, color='#181818', label='4WD', **kwargs)

      axes[i][j].set_xlabel('displacement (l)')
      axes[i][j].set_ylabel('fuel economy (mpg)')

      axes[i][j].legend(title='drive train', frameon=False)

  plt.savefig('task23.png')
  plt.show()


if __name__ == '__main__':

  kwargs = {}

  overlapping_plot(kwargs)
