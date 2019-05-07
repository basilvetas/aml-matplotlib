from os.path import join, dirname, realpath
import pandas as pd

def test_population():
	""" Tests that the world population according to
	this table in 2010 is ca. ​7065 million """
	path = realpath(join(dirname(__file__), 'input.txt'))

	kwargs = {
		'encoding': 'utf-16',
		'error_bad_lines': False,
		'index_col': 0,
		'escapechar': '\\',
		'na_values':['--']
	}

	df = pd.read_csv(path, **kwargs);

	assert round(df['2010'].astype(float, error='ignore').sum()) == 7065

if __name__ == '__main__':
	test_population()



