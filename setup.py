from setuptools import setup

setup(
	name = 'tradeinspace',
	packages=['tradeinspace'],
	include_package_date=True,
	install_requires=['flask', 'flask_sqlalchemy',
	],
)
