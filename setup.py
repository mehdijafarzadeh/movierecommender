from setuptools import setup, find_packages
import os

def open_file(fname):
    """helper function to open a local file"""
    return open(os.path.join(os.path.dirname(__file__), fname))


setup(
    name='movierecommender',
    version='0.0.1',
    author='Mehdi Jafarzadeh',
    author_email='jafrzade.me@gmail.com',
    packages=find_packages(),
    url='https://github.com/mehdijafarzadeh/movierecommender',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    description='',
    long_description=open_file('README.md').read(),
    # end-user dependencies for your library
    install_requires=[
        
    ],
)