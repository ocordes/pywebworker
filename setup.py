from setuptools import setup


#from pypovlib.pypovobjects import __version__, __author__

__version__ = '0.0.1'
__author__ = 'Oliver Cordes'

setup(
    name='pywebworker',
    version=__version__,
    author=__author__,
    #py_modules=['pywebworker'],
    packages=['pywebworker'],
    install_requires=[
     'Click',
    ],
    entry_points='''
        [console_scripts]
        pywebworker=pywebworker.app.webworkerapp:cli
    ''',
)
