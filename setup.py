from setuptools import setup, find_packages
import os


def open_file(fname):
    """helper function to open a local file"""
    return open(os.path.join(os.path.dirname(__file__), fname))


setup(
    name='mehdi_movierecommender',
    version='0.0.3',
    author='Mehdi Jafarzadeh',
    author_email='jafarzade.me@gmail.com',
    packages=find_packages(),
    url='https://github.com/mehdijafarzadeh/movierecommender',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    package_data={
        'movierecommender': ['data/ml-latest-small/*.csv', 'data/ml-latest-small/*.pickle']

    },
    description='Implementation of various collaborative filtering methods',
    long_description=open_file('README.md').read(),
    long_description_content_type='text/markdown',
    # end-user dependencies for your library
    install_requires=[
        'pandas',
        'scikit-learn',
        'fuzzywuzzy',
        'python-Levenshtein'
    ],
)
