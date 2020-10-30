# -*- coding: utf-8 -*-
"""setup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14qiqPvv0KBDP9pL7gjlHAlNE8RIJEzF7
"""

import setuptools
from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='CLUSTER_SELECTION',
      version='0.0.1',
      description='Learning setup',
      long_description= readme(),
      url='https://github.com/vineetbiyani09/ML/tree/master/CLUSTER_SELECTION',
      author='Vineet Biyani, Jash Bhatia, Yash Doshi, Sagarika Raje',
      license='MIT',
      include_package_data=True,
      package_data={
          'CLUSTER_SELECTION': ['CLUSTER_SELECTION']
      },
      packages=setuptools.find_packages(exclude=['tests']),
      zip_safe=False,
      install_requires=[ 
          "librosa>=0.8.0",
          "matplotlib>=3.2.2"
          "tensorflow>=2.3.0",
          "numpy>=1.18.5",
          "pandas>=1.1.3",
          "importlib-resources>=3.2.0",
          "scipy.cluster.hierarchy>=0.14.0",
          "sklearn.cluster>=0.22.0"
      ]
      )
