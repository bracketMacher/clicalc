from setuptools import setup


setup(
	name = 'clicalc',
	version = '0.1.0',
	packages = ['clicalc'],
	author = 'Jan-Paul',
	entry_points = {
		'console_scripts': [
			'clicalc = clicalc.__main__:main'
		]
	})