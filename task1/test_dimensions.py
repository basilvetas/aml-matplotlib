from os.path import join, dirname, realpath
import pandas as pd

def test_dimensions():
	""" Test that the number of rows in the data is 225 and
	the number of columns is 31 (using the country as an index) """
	path = realpath(join(dirname(__file__), 'input.txt'))

	kwargs = {
		'encoding': 'utf-16',
		'error_bad_lines': False,
		'index_col': 0,
		'escapechar': '\\',
		'na_values':['--']
	}

	df = pd.read_csv(path, **kwargs);

	assert df.shape[0] == 225
	assert df.shape[1] == 31

if __name__ == '__main__':
	test_dimensions()

