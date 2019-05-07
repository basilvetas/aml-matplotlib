from os.path import join, dirname, realpath
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate

path = realpath(join(dirname(__file__), 'spurrious_data.txt'))

def spurrious_plot():
	""" Recreates a plot from http://www.tylervigen.com/spurious-correlations """

	# read from a file like the assignment wants us to
	x = [] # years
	y1 = [] # worldwide non commercial space launches
	y2 = [] # sociology doctorates awarded (US)
	with open(path, 'r') as f:
		lines = f.readlines()
		x = list(map(int, lines[0].rstrip().split(',')))
		y1 = list(map(int, lines[1].rstrip().split(',')))
		y2 = list(map(int, lines[2].rstrip().split(',')))

	# this way would have been much cleaner
	# x = np.arange(1997, 2010)
	# y1 = [54, 46, 42, 50, 43, 41, 46, 39, 37, 45, 45, 41, 54]
	# y2 = [601, 579, 572, 617, 566, 547, 597, 580, 536, 579, 576, 601, 664]

	# crate the plot
	fig, ax1 = plt.subplots(figsize=(8,6))
	ax2 = ax1.twinx()

	# interplote data for smooth lines
	f1 = interpolate.interp1d(x, y1, kind='cubic')
	f2 = interpolate.interp1d(x, y2, kind='cubic')
	x_inter = np.linspace(min(x), max(x), 1000)

	ax1.plot(x, y1, 'o', x_inter, f1(x_inter), color='r')
	ax2.plot(x, y2, 'o', x_inter, f2(x_inter), color='k')

	ax1.set_ylabel('Worldwide non-commercial space launches', color='r')
	ax2.set_ylabel('Sociology doctorates awarded (US)', color='k')
	plt.xticks(x)
	plt.title('Worldwide non-commercial space launches\ncorrelates with\nSociology doctorates awarded (US)')
	plt.savefig('task21.png')
	plt.show()


if __name__ == '__main__':
	spurrious_plot()
