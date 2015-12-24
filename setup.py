from setuptools import setup

setup(name='Landscapes',
	version='0.0.1',
	description='Red social de fotografia',
	url='https://github.com/santidediego/Landscapes',
	author='Santiago de Diego, Javier Pérez',
	author_email='santidediego@gmail.com',
	license='CC0 1.0 Universal',
	install_requires=[
		'Flask',
		'Flask-Testing',
		'gunicorn',
		'itsdangerous'
		'Jinja2',
		'pymongo',
		'WTForms',
		'wheel',
        'nose',
        'Werkzeug',
        'MarkupSafe',
	],
	zip_safe=False)