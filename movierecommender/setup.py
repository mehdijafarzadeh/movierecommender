from setuptools import setup, find_packages
import os

def open_file(fname):
    """helper function to open a local file"""
    return open(os.path.join(os.path.dirname(__file__), fname))


setup(
    name='movierecommender',
    version='0.0.1',
    author='Malte Bonart',
    author_email='malte@spiced-academy.com',
    packages=find_packages(),
    url='https://github.com/bonartm/movierecommender',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    description='Implementation of various collaborative filtering methods',
    long_description=open_file('README.md').read(),
    # end-user dependencies for your library
    install_requires=[
        'pandas',
        'scikit-learn',
        'fuzzywuzzy',
        'python-Levenshtein'        
    ],
)
