# -*- coding: utf-8 -*-
"""
Setup script.
Created on Sat May 11 22:00:00 2019
Author: Prasun Roy | CVPRU-ISICAL (http://www.isical.ac.in/~cvpr)
GitHub: https://github.com/prasunroy/nnview

"""


try:
    from setuptools import setup
except:
    from distutils.core import setup


setup(name='nnview',
      version='0.1.0',
      description='Visualization utilities for PyTorch',
      long_description=open('README.md').read(),
      author='Prasun Roy',
      author_email='prasunroy.pr@gmail.com',
      url='https://github.com/prasunroy/nnview',
      download_url='github.com/prasunroy/nnview/tarball/0.1.0',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities'
      ],
      keywords=[
          'deep-learning',
          'visualization',
          'pytorch',
          'torchvision'
      ],
      packages=['nnview'])
