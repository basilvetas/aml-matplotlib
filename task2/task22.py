import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
from sklearn import datasets

iris = datasets.load_iris()

def pair_plot(scatter_kwargs, hist_kwargs):
  """ generates scatterplot matrix with histograms of iris dataset """
  dim = len(iris['feature_names'])

  # create layout
  fig, axes = plt.subplots(dim, dim, figsize=(10,10))

  # remove gaps between subplots
  fig.subplots_adjust(wspace=0, hspace=0)

  # iterate over each subplot and plot data
  for i, a in zip(list(range(dim)), iris['feature_names']):
    for j, b in zip(list(range(dim)), iris['feature_names']):
      ax = axes[i, j]

      # if diagonal, plot a histogram
      if i == j:
        ax.hist(iris['data'].T[i], **hist_kwargs)

      # otherwise plot a scatterplot
      else:
        ax.scatter(iris['data'].T[j], iris['data'].T[i], **scatter_kwargs)

      ax.set_xlabel(b)
      ax.set_ylabel(a)

      if j != 0:
        ax.yaxis.set_visible(False)
      if i != dim - 1:
        ax.xaxis.set_visible(False)

  # add legend
  setosa = mpatches.Patch(color='#0000aa', label='Setosa')
  versicolor = mpatches.Patch(color='#ff2020', label='Versicolor')
  virginica = mpatches.Patch(color='#50ff50', label='Virginica')
  plt.legend(handles=[setosa, versicolor, virginica])

  plt.savefig('task22.png')
  plt.show()

if __name__ == '__main__':
  scatter_kwargs = {
    'c': iris['target'],
    'marker': 'o',
    's': 60,
    'alpha': .8,
    'cmap': ListedColormap(['#0000aa', '#ff2020', '#50ff50'])
  }

  hist_kwargs = {
    'bins': 20,
    'color':'#0000aa'
  }

  pair_plot(scatter_kwargs, hist_kwargs)
